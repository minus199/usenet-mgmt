"""
SAB_SCRIPT	The name of the current script
SAB_NZO_ID	The unique ID assigned to the job
SAB_FINAL_NAME	The name of the job in the queue and of the final folder
SAB_FILENAME	The NZB filename (after grabbing from the URL)
SAB_COMPLETE_DIR	The whole path to the output directory of the job
SAB_PP_STATUS	Was post-processing succesfully completed (repair and/or unpack, if enabled by user)
SAB_CAT	What category was assigned
SAB_BYTES	Total number of bytes
SAB_BYTES_TRIED	How many bytes of the total bytes were tried
SAB_BYTES_DOWNLOADED	How many bytes were recieved (can be more than tried, due to overhead)
SAB_DUPLICATE	Was it detected as duplicate
SAB_UNWANTED_EXT	Were there unwanted extensions
SAB_OVERSIZED	Was the job over the user's size limit
SAB_PASSWORD	What was the password supplied by the NZB or the user
SAB_ENCRYPTED	Was the job detected as encrypted
SAB_STATUS	Current status (completed/failed/running)
SAB_FAIL_MSG	If job failed, why did it fail
SAB_AGE	Average age of the articles in the post
SAB_URL	URL from which the NZB was retrieved
SAB_AVG_BPS	Average bytes/second speed during active downloading
SAB_DOWNLOAD_TIME	How many seconds did we download
SAB_PP	What post-processing was activated (download/repair/unpack/delete)
SAB_REPAIR	Was repair selected by user
SAB_UNPACK	Was unpack selected by user
SAB_FAILURE_URL	Provided by some indexers as alternative NZB if download fails
SAB_PRIORITY	Priority set by user
SAB_GROUP	Newsgroup where (most of) the job's articles came from
SAB_VERSION	The version of SABnzbd used
SAB_ORIG_NZB_GZ	Path to the original NZB-file of the job. The NZB-file is compressed with gzip (.gz)
SAB_PROGRAM_DIR	The directory where the current SABnzbd instance is located
SAB_PAR2_COMMAND	The path to the par2 command on the system that SABnzbd uses
SAB_MULTIPAR_COMMAND	Windows-only (empty on other systems). The path to the MultiPar command on the system that SABnzbd uses
SAB_RAR_COMMAND	The path to the unrar command on the system that SABnzbd uses
SAB_ZIP_COMMAND	The path to the unzip command on the system that SABnzbd uses
SAB_7ZIP_COMMAND	The path to the 7z command on the system that SABnzbd uses. Not all systems have 7zip installed (it's optional for SABnzbd), so this can also be empty
"""