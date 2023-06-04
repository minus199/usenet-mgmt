const fs = require("fs/promises")
const parser = require('episode-parser')
const titleCase = require("./titleCase")



async function scan(src, target, output = {}) {
    const listingGen = await fs.opendir(src)

    for await (const ent of listingGen) {
        const { show, season, episode, ...meta } = parser(ent.name)
        const isSeasonDir = !episode

        const computedTargetDir = `${target}/${titleCase(show.toLowerCase())}/Season ${season}`
        const descriptor = {
            source: `${src}/${ent.name}`,
            target: computedTargetDir,
            isSeasonDir
        }

        const container = output[computedTargetDir] = output[computedTargetDir] || []
        container.push(descriptor)

        await fs.mkdir(computedTargetDir, { recursive: true })
    }

    return output
}

async function main() {
    const base = "/media/minus/media.storage.2/storage/media-server/downloads/complete"
    const srcDir = `${base}/tv`
    const targetDir = `${base}/tv-sorted`



    const listingsBySeason = await scan(srcDir, targetDir)
    const a = Object.entries(listingsBySeason)
        // .map(([source, item]) => `mv ${item.reduce((acc, curr) => `${acc} \\\n\t${curr.target}`, item)} \\\n\t${source}`)

    
    fs.writeFile(`./genereted_move_script_${Date.now()}`, a.join('\n\n'))
}

main()