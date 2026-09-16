# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *

class DummyDeFiVault(gl.Contract):
    aegis_guardian: Address
    is_paused: bool

    def __init__(self, aegis_address: str):
        self.aegis_guardian = Address(aegis_address)
        self.is_paused = False

    @gl.public.write
    def emergency_pause(self) -> None:
        if gl.message.sender_address != self.aegis_guardian:
            raise gl.vm.UserError("Unauthorized: Only Aegis can pause this protocol.")
        self.is_paused = True

    @gl.public.view
    def get_status(self) -> str:
        return "PAUSED" if self.is_paused else "ACTIVE"
