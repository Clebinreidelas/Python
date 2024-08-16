import instapy
from instapy import InstaPy
from instapy import smart_run

insta_username=""
insta_password= ''

session = InstaPy(username=insta_username,password=insta_password,headless_browser=False)
with smart_run(session):


    session.set_dont_include(['fiend1','friend2'])

    session.like_by_tags(['python','corinthians'])

    session.join_pods(topic='games ',engagaement_mode='no comments')