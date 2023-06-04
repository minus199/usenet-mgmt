docker inspect -f {{ index .Config.Labels "build_version" }} sabnzbd
