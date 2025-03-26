from core.core.utils.collections import deep_update
from core.core.utils.settings import get_settings_from_environment


"""
This takes env variables with a matching prefix, script out the prefix,
and it's global
export CORESETTINGS_IN_DOCKER=true (environvariables)
"""

# globals() is a dictionary of global variables
deep_update(
    globals(),
    get_settings_from_environment(
        ENVVAR_SETTINGS_PREFIX  # noqa
    )  # type: ignore
)
