var path = require('path');
var webpack = require('webpack');
var outputPath = '../static/javascript/';

module.exports = {
    entry: {
        preload: '../compiled-components/index.js'
    },
    output: {
        path: outputPath,
        publicPath: outputPath,
        filename: '[name].bundle.js',
        chunkFilename: '[id].bundle.js'
    },
    node: {
        fs: "empty"
    }
};