import tidalapi

copy_id = None

session1 = tidalapi.Session()
print('[FROM] Open this link in your browser:')
session1.login_oauth_simple()
usr1 = session1.user

session2 = tidalapi.Session()
print('[TO] Open this link in your browser:' )
session2.login_oauth_simple()
usr2 = session2.user


# get list tracks in the playlist
def getTracksInPlaylist(session,playlist_id):
    playlist = session.playlist(playlist_id)
    tracks = playlist.tracks()
    listTrack = []
    for track in tracks:
        listTrack.append(str(track.id))
    return listTrack

if(copy_id == None):
    playlists = usr1.playlists()
    for playlist in playlists:
        playlist2 = usr2.create_playlist("Copy of " + playlist.name, "Create by levandong.com")
        playlist2.add(getTracksInPlaylist(session1,playlist.id))
else:
    playlist_copy = session1.playlists(copy_id)
    playlist2 = usr2.create_playlist("Copy of " + playlist_copy.name, "Create by levandong.com")
    playlist2.add(getTracksInPlaylist(session1,playlist_copy.id))

