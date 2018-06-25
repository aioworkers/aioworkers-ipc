import posix_ipc

from aioworkers.core.base import ExecutorEntity
from aioworkers.core.formatter import FormattedEntity
from aioworkers.queue.base import AbstractQueue, score_queue


@score_queue(default_score=0)
class Queue(FormattedEntity, ExecutorEntity, AbstractQueue):
    def set_context(self, context):
        context.on_stop.append(self.stop)
        super().set_context(context)

    def set_config(self, config):
        c = config.new_child(executor=1)
        super().set_config(c)
        self._queue = posix_ipc.MessageQueue(
            self.config.key, posix_ipc.O_CREAT,
            max_messages=self.config.get_int('max_messages', default=posix_ipc.QUEUE_MESSAGES_MAX_DEFAULT),
            max_message_size=self.config.get_int('max_message_size', default=posix_ipc.QUEUE_MESSAGE_SIZE_MAX_DEFAULT),
        )
        self._timeout_put = self.config.get_float('timeout.put', null=True, default=None)
        self._timeout_get = self.config.get_float('timeout.get', null=True, default=None)

    async def get(self):
        val, score = await self.run_in_executor(self._queue.receive, self._timeout_get)
        value = self.decode(val)
        return score, value

    async def put(self, value):
        score, val = value
        val = self.encode(val)
        await self.run_in_executor(self._queue.send, val, self._timeout_put, score or 0)

    async def stop(self):
        try:
            self._queue.close()
        except AttributeError:
            pass
