import os
import shutil

BUILD_DIR = "docs"

def main():
    make_build_dir()
    # copy_res_folder()

    for page_file in os.listdir("pages"):
        page_html = get_html_from_file(f"pages/{page_file}")
        page_html = page_html.replace("{{ VIDEOS }}", get_all_videos_html_list())
        write_html_to_file(page_html, page_file)


def apply_navbar(html: str) -> str:
    return html.replace(
        "{{ NAVBAR }}",
        get_html_from_file("templates/nav.html")
    )

def get_html_from_file(file: str) -> str:
    with open(file, "r") as f:
        return f.read()

def write_html_to_file(html: str, file: str) -> None:
    with open(f"{BUILD_DIR}/{file}", "w+") as f:
        f.write(html)

def copy_res_folder() -> None:
    shutil.copytree("res", f"{BUILD_DIR}/res")

def make_build_dir() -> None:
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)

    os.makedirs(BUILD_DIR)

def get_videos_list() -> list[str]:
    with open("videos_list.txt") as f:
        return f.read().split("\n")[:-1]

def get_all_videos_html_list() -> str:
    videos_url_list = get_videos_list()
    return '\n'.join(
        [get_single_video_html(url) for url in videos_url_list]
    )

def get_single_video_html(url: str) -> str:
    html = get_html_from_file("templates/single_video.html")
    html = html.replace("{{ URL }}", url)
    html = html.replace("{{ NAME }}", url)
    return html

if __name__ == '__main__':
    main()
