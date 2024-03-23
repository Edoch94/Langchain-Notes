import logging
import logging.config
import os
from datetime import datetime
from pathlib import Path

from omegaconf import DictConfig, OmegaConf


def load_config(*config_files: Path) -> DictConfig:
    """Load the configuration files and merge them into a single configuration

    :param config_files: list of paths to the configuration files
    :type config_files: list[Path]
    :return: merged configuration
    :rtype: DictConfig | ListConfig
    """
    configs = [OmegaConf.load(file) for file in config_files]
    configs.append(OmegaConf.from_cli())
    config = OmegaConf.merge(*configs)
    OmegaConf.resolve(config)
    if not isinstance(config, DictConfig):
        raise ValueError('"config_files" should be dictionaries')
    return config


def setup_logging(*logging_config_files: Path) -> Path:
    """Setup the logging using the configuration files provided as arguments

    :param logging_config_files: list of paths to the logging configuration files
    :type logging_config_files: list[Path]
    :return: path to the log file
    :rtype: Path
    """

    logging_config = load_config(*logging_config_files)
    logging_config = OmegaConf.to_container(cfg=logging_config, resolve=True)
    if not isinstance(logging_config, dict):
        raise ValueError('logging_config should be a dictionary')
    logging_config = {str(key): value for key, value in logging_config.items()}
    log_path: Path | None = None
    for handler in logging_config['handlers'].values():
        match handler:
            case {'class': 'logging.FileHandler', 'filename': filename}:
                log_file_path = Path(filename)
                log_path = log_file_path.parent
                log_path.mkdir(parents=True, exist_ok=True)
                log_file_path.touch(exist_ok=False)

    logging.config.dictConfig(logging_config)

    if log_path is None:
        raise ValueError('No log file path found in the logging configuration files')

    return log_path


def main() -> None:
    """Main function"""

    os.environ['STARTDATETIME'] = f'{datetime.now():%Y-%m-%d/%H-%M-%S}'
    logger = logging.getLogger('langchain_notes')

    log_path = setup_logging(Path('configs/logging/config.yaml'))  # noqa: F841

    logger.info('Entering "main"')

    cfg = load_config(Path('configs/project/main.yaml'))  # noqa: F841

    logger.info('Exiting "main"')


if __name__ == '__main__':
    main()
