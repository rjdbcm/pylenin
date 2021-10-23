from dataclasses import dataclass
import requests
import json

__title__ = 'PyLenin'
__version__ = '0.0.2'
__author__ = 'Ross J. Duff'
__license__ = "GPL"
__apiversion__ = '0.1'

@dataclass
class remoteError:
    code: int
    error: str


@dataclass
class NewReq:
    title: str
    text: str
    expiration: str


@dataclass
class NewResp:
    name: str


@dataclass
class GetRespInfo:
    create_time: int
    delete_time: int
    title: str


@dataclass
class GetResp:
    name: str
    text: str
    info: GetRespInfo


@dataclass
class AboutResp:
    exist: bool
    text: str


@dataclass
class RulesResp:
    exist: bool
    text: str


@dataclass
class VersionResp:
    version: str
    git_tag: str
    git_commit: str
    build_date: str


def http_error_check(resp):
    if resp.status_code == 200:
        return resp.status_code
    else:
        raise requests.HTTPError(resp)


def get_url(url: str) -> bytes:
    out: bytes
    resp = requests.get(url)
    out = resp.content
    http_error_check(resp)
    return out


def post_url(url: str, params) -> bytes:
    resp = requests.post(url, params=params)
    out = resp.content
    http_error_check(resp)
    return out


def new(req: NewReq, base_url: str) -> NewResp:

    vals = {
        "title": req.title,
        "text": req.text,
        "expiration": req.expiration
            }

    return post_url(base_url + '/new', params=vals)


def get(name: str, base_url: str) -> GetResp:
    return get_url(base_url + '/get/' + name)


def about(base_url: str) -> AboutResp:
    return get_url(base_url + '/about')


def rules(base_url: str) -> RulesResp:
    return get_url(base_url + '/rules')


def version(base_url: str) -> VersionResp:
    return get_url(base_url + '/version')
