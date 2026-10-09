from uuid import UUID

from shortuuid import decode, encode


class ShortUuidGenerator:

    async def get_short_id(self, uuid: UUID):

        short_id = encode(uuid)
        print(short_id)
        return short_id

    async def get_uuid(self, short_id: str) -> UUID:

        uuid = decode(short_id)
        print(uuid)
        return uuid
