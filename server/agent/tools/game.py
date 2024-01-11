
from pydantic import BaseModel, Field

def game(name: str):
    print(f"introduce_game:{name}")
    return name

class GameInput(BaseModel):
    name: str = Field()

if __name__ == "__main__":
    result = game("王者荣耀")
    print("游戏:",result)