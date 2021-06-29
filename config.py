from typing import Literal, Optional
import pydantic

EnvContext = Literal['local', 'prod', 'stage']
EnvBrowserName = Literal['chrome', 'firefox']


class Settings(pydantic.BaseSettings):
    # below are parameters that reads from os env
    context: EnvContext = 'local'
    browser_config_timeout: int = 7
    browser_name: EnvBrowserName = 'chrome'
    browser_quit_after_each_test: bool = False
    browser_headless: bool = False
    browser_window_maximize: bool = False
    browser_window_width: int = 1024
    browser_window_height: int = 768
    remote_url: Optional[pydantic.AnyHttpUrl] = None
    remote_enableVNC: bool = True
    remote_screenResolution: str = '1024x768x16'


settings = Settings(_env_file=f'config.{Settings().context}.env')

if __name__ == '__main__':
    print(settings.__repr__())
