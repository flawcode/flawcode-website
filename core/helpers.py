import os

def show_notes(ep_no):
    filename = "core/show_notes/" + str(ep_no) + ".md"
    with open(filename) as f:
        return f.read()


def get_last_4episode_num(ep_count):
    # python needs +1
    ep_count += 1
    return reversed(range(ep_count)[-4:])


def episode_title(episode_num):
    """Episode title for the respective episode

    :episode_num: int
    :returns: str
        title of the episode taken from the markdown

    """
    with open('core/show_notes/{}.md'.format(str(episode_num))) as f:
        title_line = f.readline().rstrip()
    title_line = title_line.replace("# ", "")
    title_line = title_line.replace("## ", "")
    title_line = title_line.replace("#", "")
    return title_line


def get_archives_content(ep_count):
    """The list of past urls that will go to the archive section.

    :ep_count: int
        The present count of the total number of episodes present.
    :returns: str
        html string with the list of the episodes.

    """
    return [(i, episode_title(i)) for i in reversed(range(1, ep_count - 3))]


def mp3_file_sizes(mp3_dir='core/static/audio'):
    """Create a dictionary with the sizes of the mp3 files
    :returns: dict
        {mp3filename: filesize}

    """
    files = {}
    for file in os.listdir(mp3_dir):
        if file.endswith(".mp3"):
            filepath = os.path.join(mp3_dir, file)
            file_size = os.stat(filepath).st_size /(1024*1024.0)
            files[file.replace('.mp3', '')] = (
                "{0:.2f}"
                .format(round(file_size,2)))
    return files
