class MustHaveLicenseError(Exception):
    pass


class CurrentViewCountOverFourError(Exception):
    pass


def display_video(video, user):
    try:
        video = get_video(video, user)
    except MustHaveLicenseError:
        ...  # 사용권 구매 페이지로 이동
    except CurrentViewCountOverFourError:
        ...  # 메인 페이지로 이동


def get_video(video, user):
    if not user.has_licensed():
        raise MustHaveLicenseError("사용권이 있어야만 볼 수 있습니다") # -> 사용권 구매 페이지로 이동 시킴
    elif user.license.current_view_count >= 4:
        raise CurrentViewCountOverFourError("현재 시청자 수가 많아 볼 수 없습니다") # -> 메인 페이지로 이동 시킴
    return get_video_contents(video)


def get_video_contents(video):
    ...
    return video

