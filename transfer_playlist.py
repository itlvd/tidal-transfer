import tidalapi
import os
#===================Setup variable=====================
copy_id = '6302ac36-9501-4d52-aaad-e632ae18a786' # playlist id. Set copy_id = None if you want to copy all.
#======================================================
os.system("clear")
session1 = tidalapi.Session()
print('[FROM] Open this link in your browser:')
session1.login_oauth_simple()
assert(session1.check_login() == True)
usr1 = session1.user
os.system("clear")

session2 = tidalapi.Session()
print('[TO] Open this link in your browser:' )
session2.login_oauth_simple()
assert(session2.check_login() == True)
usr2 = session2.user
os.system("clear")

# get list tracks in the playlist
def getTracksInPlaylist(session,playlist_id):
    playlist = session.playlist(playlist_id)
    tracks = playlist.tracks()
    listTrack = []
    for track in tracks:
        print("Copy music:", track.name)
        listTrack.append(str(track.id))
    return listTrack

if(copy_id == None or copy_id == ""):
    playlists = usr1.playlists()
    for playlist in playlists:
        playlist2 = usr2.create_playlist("Copy of " + playlist.name, "Create by levandong.com")
        print("Copy playlist", playlist.name)
        playlist2.add(getTracksInPlaylist(session1,playlist.id))
else:
    playlist_copy = session1.playlist(copy_id)
    playlist2 = usr2.create_playlist("Copy of " + playlist_copy.name, "Create by levandong.com")
    print("Copy playlist", playlist_copy.name)
    playlist2.add(getTracksInPlaylist(session1,playlist_copy.id))