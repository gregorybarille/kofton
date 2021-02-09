const path = require('path');
module.exports = {
    // disable hashes in filenames
    filenameHashing: false,
    outputDir: path.resolve(__dirname, "../back/kofton_statics/"),
    chainWebpack: config => {
        config.plugins.delete('html')
    }
}