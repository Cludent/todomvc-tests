from typing import Literal
import pydantic

EnvContext = Literal['local', 'prod', 'stage']
EnvBrowserName = Literal['chrome', 'firefox']

class Options(pydantic.BaseSettings):

    context: EnvContext = 'local'

    browser_config_timeout: int = 7
    browser_name: EnvBrowserName = 'chrome'
    browser_headless: bool = False
    browser_quit_after_each_test: bool = False


options = Options(_env_file=f'config.{Options().context}.env')

if __name__ == '__main__':
    print(options.__repr__())
