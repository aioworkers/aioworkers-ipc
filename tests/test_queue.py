from pathlib import Path

import pytest
from aioworkers.core.config import Config
from aioworkers.core.context import Context


@pytest.fixture
def config():
    c = Config()
    p = Path(__file__).parent / 'q.ini'
    c.load(p)
    return c


async def test_q(loop, config):
    async with Context(config, loop=loop) as ctx:
        await ctx.queue.put(1)
        assert 1 == await ctx.queue.get()
