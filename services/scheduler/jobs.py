from services.blocks import BlockService


async def remove_expired_blocks_job(block_service: BlockService) -> None:
    await block_service.remove_expired_blocks()
