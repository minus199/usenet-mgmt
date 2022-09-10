set -e

if docker exec "${CONTAINER}" sh -c "test -f ${PROV_CHK_PNT} && echo 'Already provisioned.'"; then
    exit
fi

echo "Installing python deps on ${CONTAINER}..."
docker exec "${CONTAINER}" /usr/bin/python3 -m pip install --upgrade pip
docker exec "${CONTAINER}" /usr/bin/python3 -m pip install setuptools
docker exec "${CONTAINER}" /usr/bin/python3 -m pip install subliminal ipython

echo "Creating root common directory..."
docker exec "${CONTAINER}" sh -c "mkdir -p $COMMON_MODULES_PATH_DEST && chown abc:abc $COMMON_MODULES_PATH_DEST"

echo "Copying from $MAIN_SCRIPT_SRC_PATH to ${CONTAINER}:${SCRIPTS_PATH_DEST}..."
docker cp "${MAIN_SCRIPT_SRC_PATH}" "${CONTAINER}:${SCRIPTS_PATH_DEST}"
docker exec "${CONTAINER}" sh -c "chmod +x ${MAIN_SCRIPT_DEST_PATH}"

echo "Copying from ${COMMON_MODULES_PATH_SRC} to ${CONTAINER}:${COMMON_MODULES_PATH_DEST}..."
docker cp "${COMMON_MODULES_PATH_SRC}" "${CONTAINER}:${COMMON_MODULES_PATH_DEST}/"

echo "Adding ${COMMON_MODULES_PATH_DEST} to python path"
docker exec "${CONTAINER}" sh -c "echo /xmodules/ > /usr/local/lib/python3.6/dist-packages/xmods.pth"

if docker exec "${CONTAINER}" sh -c "test -z '${PYTHONPATH}'"; then
    docker exec "${CONTAINER}" sh -c "echo export PYTHONPATH='${COMMON_MODULES_PATH_DEST}/' >> ~/.bashrc"
else
    pypath=`docker exec "${CONTAINER}" sh -c 'echo $PYTHONPATH'`
    docker exec "${CONTAINER}" sh -c "echo export PYTHONPATH='${pypath}:${COMMON_MODULES_PATH_DEST}/' >> ~/.bashrc"
fi

echo "Creating checkpoint"
docker exec "${CONTAINER}" touch $PROV_CHK_PNT