class DefaultColor:
    """
    This class should have the default colors for every segment.
    Please test every new segment with this theme first.
    """
    USERNAME_FG = 15 # white
    USERNAME_BG = 31 # light blue
    USERNAME_ROOT_BG = 88 # darkish red

    HOSTNAME_FG = 250
    HOSTNAME_BG = 236

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = 238  # medium-dark grey
    HOME_FG = 15  # white
    PATH_BG = 240  # medium grey
    PATH_FG = 250  # light grey
    CWD_FG = 15  # nearly-white grey
    SEPARATOR_FG = 244

    READONLY_BG = 88
    READONLY_FG = 254

    SSH_BG = 166 # medium orange
    SSH_FG = 254

    REPO_CLEAN_BG = 2  # a light green color
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 52  # pink/red
    REPO_DIRTY_FG = 15  # white

    JOBS_FG = 39
    JOBS_BG = 237

    CMD_PASSED_BG = 236
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 94
    CMD_FAILED_FG = 226

    SVN_CHANGES_BG = 148
    SVN_CHANGES_FG = 22  # dark green

    GIT_AHEAD_BG = 240
    GIT_AHEAD_FG = 250
    GIT_BEHIND_BG = 240
    GIT_BEHIND_FG = 250
    GIT_STAGED_BG = 22
    GIT_STAGED_FG = 15
    GIT_NOTSTAGED_BG = 130
    GIT_NOTSTAGED_FG = 15
    GIT_UNTRACKED_BG = 52
    GIT_UNTRACKED_FG = 15
    GIT_CONFLICTED_BG = 9
    GIT_CONFLICTED_FG = 15

    VIRTUAL_ENV_BG = 39  # a mid-tone green
    VIRTUAL_ENV_FG = 17

class Color(DefaultColor):
    """
    This subclass is required when the user chooses to use 'default' theme.
    Because the segments require a 'Color' class for every theme.
    """
    pass
