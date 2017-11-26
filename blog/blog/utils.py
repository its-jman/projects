import os


def get_push_time():
    """
    Gets the time that the last git pull was executed on this project.
    :return: String to display on page
    """

    try:
        with open(os.getcwd() + '/times/blog_time', 'r') as time_file:
            read_time = time_file.readline().rstrip('\n')
            return read_time
    except IOError:
        return 'Failed to retrieve time.'
