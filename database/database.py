# database.py (version locale, sans MongoDB)
import json
import asyncio
import os

DB_FILE = "local_db.json"
LOCK = asyncio.Lock()

def _load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    else:
        return {
            "channels": {},
            "admins": {},
            "users": {},
            "banned_user": {},
            "autho_user": {},
            "del_timer": {"value": 600},
            "fsub": {},
            "request_forcesub": {},
            "request_forcesub_channel": {}
        }

def _save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

class Rohit:
    def __init__(self, DB_URI=None, DB_NAME=None):  # kept for compatibility
        self.data = _load_data()

    # === USER DATA ===
    async def present_user(self, user_id: int):
        async with LOCK:
            return str(user_id) in self.data["users"]

    async def add_user(self, user_id: int):
        async with LOCK:
            self.data["users"][str(user_id)] = True
            _save_data(self.data)

    async def full_userbase(self):
        async with LOCK:
            return list(map(int, self.data["users"].keys()))

    async def del_user(self, user_id: int):
        async with LOCK:
            self.data["users"].pop(str(user_id), None)
            _save_data(self.data)

    # === ADMIN DATA ===
    async def admin_exist(self, admin_id: int):
        async with LOCK:
            return str(admin_id) in self.data["admins"]

    async def add_admin(self, admin_id: int):
        async with LOCK:
            self.data["admins"][str(admin_id)] = True
            _save_data(self.data)

    async def del_admin(self, admin_id: int):
        async with LOCK:
            self.data["admins"].pop(str(admin_id), None)
            _save_data(self.data)

    async def get_all_admins(self):
        async with LOCK:
            return list(map(int, self.data["admins"].keys()))

    # === BANNED USERS ===
    async def ban_user_exist(self, user_id: int):
        async with LOCK:
            return str(user_id) in self.data["banned_user"]

    async def add_ban_user(self, user_id: int):
        async with LOCK:
            self.data["banned_user"][str(user_id)] = True
            _save_data(self.data)

    async def del_ban_user(self, user_id: int):
        async with LOCK:
            self.data["banned_user"].pop(str(user_id), None)
            _save_data(self.data)

    async def get_ban_users(self):
        async with LOCK:
            return list(map(int, self.data["banned_user"].keys()))

    # === DELETE TIMER ===
    async def set_del_timer(self, value: int):
        async with LOCK:
            self.data["del_timer"]["value"] = value
            _save_data(self.data)

    async def get_del_timer(self):
        async with LOCK:
            return self.data["del_timer"].get("value", 600)

    # === CHANNEL MANAGEMENT ===
    async def channel_exist(self, channel_id: int):
        async with LOCK:
            return str(channel_id) in self.data["fsub"]

    async def add_channel(self, channel_id: int):
        async with LOCK:
            self.data["fsub"][str(channel_id)] = {"mode": "off"}
            _save_data(self.data)

    async def rem_channel(self, channel_id: int):
        async with LOCK:
            self.data["fsub"].pop(str(channel_id), None)
            _save_data(self.data)

    async def show_channels(self):
        async with LOCK:
            return list(map(int, self.data["fsub"].keys()))

    async def get_channel_mode(self, channel_id: int):
        async with LOCK:
            return self.data["fsub"].get(str(channel_id), {}).get("mode", "off")

    async def set_channel_mode(self, channel_id: int, mode: str):
        async with LOCK:
            self.data["fsub"].setdefault(str(channel_id), {})["mode"] = mode
            _save_data(self.data)

    # === FORCE SUB REQUESTS ===
    async def req_user(self, channel_id: int, user_id: int):
        async with LOCK:
            ch = self.data["request_forcesub_channel"].setdefault(str(channel_id), {"user_ids": []})
            if user_id not in ch["user_ids"]:
                ch["user_ids"].append(user_id)
                _save_data(self.data)

    async def del_req_user(self, channel_id: int, user_id: int):
        async with LOCK:
            ch = self.data["request_forcesub_channel"].get(str(channel_id))
            if ch and user_id in ch["user_ids"]:
                ch["user_ids"].remove(user_id)
                _save_data(self.data)

    async def req_user_exist(self, channel_id: int, user_id: int):
        async with LOCK:
            ch = self.data["request_forcesub_channel"].get(str(channel_id), {})
            return user_id in ch.get("user_ids", [])

    async def reqChannel_exist(self, channel_id: int):
        return await self.channel_exist(channel_id)


# Remplacer Mongo client par objet local
db = Rohit()