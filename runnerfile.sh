#!/bin/bash

# echo ${@} -- get flags

export CONTAINER="sabnzbd"
export SCRIPTS_PATH_DEST="/app/sabnzbd/scripts"

export MODULES_PATH_SRC="$(dirname `dirname "$(realpath ${BASH_SOURCE[0]})"`)"
export MAIN_SCRIPT_NAME="subtitles_postproc.py"
export MAIN_SCRIPT_SRC_PATH="${MODULES_PATH_SRC}/${MAIN_SCRIPT_NAME}"
export MAIN_SCRIPT_DEST_PATH="${SCRIPTS_PATH_DEST}/${MAIN_SCRIPT_NAME}"
export COMMON_MODULES_PATH_SRC=`realpath ${MODULES_PATH_SRC}/common`
export COMMON_MODULES_PATH_DEST="/xmodules"
export PROV_CHK_PNT="/app/provisoned.chkpnt"

task_stop() {
    docker-compose -f sabnzbd.compose.yml -p usenet stop
}

task_up() {
    docker-compose -f sabnzbd.compose.yml -p usenet up -d
}

task_provision(){
    source `dirname "$(realpath ${BASH_SOURCE[0]})"`/provision.sh
}

task_clean_prov(){
    docker exec "${CONTAINER}" sh -c "rm -rf ${COMMON_MODULES_PATH_DEST} ${PROV_CHK_PNT} ${MAIN_SCRIPT_DEST_PATH} '~/.bashrc'"
}