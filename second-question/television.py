"""
Construa uma classe em Python que represente uma televisão. Deve ser possível:

- Alterar os canais
- Alterar o volume
- Alternar a função 'mudo'
"""

from readchar import readchar
from typing import Literal
import os

class TelevisionChannels:
    __max_channel = 100
    __min_channel = 1

    __channel: int = 1

    def __init__(self) -> None:
        pass
    
    def next_channel(self) -> None:
        new_channel = self.__channel + 1
        if new_channel <= self.__max_channel:
            self.__channel = new_channel

    def previous_channel(self) -> None:
        new_channel = self.__channel -1
        if new_channel >= self.__min_channel:
            self.__channel = new_channel

    def get_channel(self) -> None:
        return self.__channel


class TelevisionVolume:
    __volume: int = 30
    __muted: bool = False

    __max_volume = 100
    __min_volume = 0

    def __init__(self) -> None:
        pass

    def is_muted(self) -> bool:
        return self.__muted

    def toggle_mute(self) -> None:
        if self.__muted:
            self.__muted = False
            return

        self.__muted = True

    def __unmute(self) -> None:
        if self.__muted:
            self.__muted = False

    def get_volume(self) -> int:
        return self.__volume

    def volume_up(self) -> None:
        new_volume = self.__volume + 1
        if new_volume <= self.__max_volume:
            self.__unmute()
            self.__volume = new_volume

    def volume_down(self) -> None:
        new_volume = self.__volume - 1
        if  new_volume >= self.__min_volume:
            self.__unmute()
            self.__volume = new_volume
            
            
class TelevisionScreen:
    def __init__(self) -> None:
        pass

    def __command_list_str(self) -> str:
        return """
- Aumentar volume: "w"
- Diminuir volume: "s"
- Último canal: "a"
- Próximo canal: "d"
- Mutar: "m"
- Desligar televisão: "p"
        """.strip()

    def __format_number(self, number: int) -> str:
        if number == 100:
            return f'{number}'
        if number < 100 and number >= 10:
            return f'0{number}'
        
        return f'00{number}'
    
    def __clear_screen(self) -> None:
        os.system("cls" if os.name == 'nt' else 'clear')

    def show_screen(self, volume: int, channel: int, muted: bool) -> None:
        self.__clear_screen()

        if muted:
            print(f"""
|--------------------------------------|
|                                      |
|           CANAL {self.__format_number(channel)}                  |
|           VOLUME MUDO                |
|                                      |
|--------------------------------------| 

{self.__command_list_str()}
        """.strip())
            return

        print(f"""
|--------------------------------------|
|                                      |
|           CANAL {self.__format_number(channel)}                  |
|           VOLUME {self.__format_number(volume)}                 |
|                                      |
|--------------------------------------| 

{self.__command_list_str()}
        """.strip())


TelevisionRemoteCommand = Literal['volume-up', 'volume-down', 'next-channel', 'previous-channel', 'mute', 'power']

            
class TelevisionRemote:
    def __init__(self) -> None:
        pass

    def __interpret_command(self, char: str) -> TelevisionRemoteCommand | None:
        match char:
            case "w":
                return 'volume-up'
            case "s":
                return 'volume-down'
            case "a":
                return 'previous-channel'
            case "d":
                return 'next-channel'
            case "m":
                return 'mute'
            case "p":
                return 'power'
            
        return None

    def wait_for_command(self) ->  TelevisionRemoteCommand | None:
        char = readchar()
        return self.__interpret_command(char) 


class Television:
    __power: bool = True

    __volume_module = TelevisionVolume()
    __channels_module = TelevisionChannels()
    __screen_module = TelevisionScreen()
    __remote_module = TelevisionRemote()

    def __init__(self) -> None:
        pass

    def __show_screen(self) -> None:
        self.__screen_module.show_screen(
            self.__volume_module.get_volume(),
            self.__channels_module.get_channel(),
            self.__volume_module.is_muted(),
        )

    def __power_off(self) -> None:
        self.__power = False

    def __exec_command(self, command: TelevisionRemoteCommand) -> None:
        match command:
            case 'power':
                self.__power_off()
            case 'mute':
                self.__volume_module.toggle_mute()
            case 'volume-up':
                self.__volume_module.volume_up()
            case 'volume-down':
                self.__volume_module.volume_down()
            case 'next-channel':
                self.__channels_module.next_channel()
            case 'previous-channel':
                self.__channels_module.previous_channel()

    def power_on(self):
        while self.__power:
            self.__show_screen()

            command = self.__remote_module.wait_for_command()
            if command:
                self.__exec_command(command)
    

if __name__ == '__main__':
    television = Television()
    television.power_on()
