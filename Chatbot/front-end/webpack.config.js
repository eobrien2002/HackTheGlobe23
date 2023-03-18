module.exports = {
  module: {
    loaders: [
      { 
        test: /\.html$/,
        exclude: /node_modules/,
        include: /src/User/Shared/ + /assests/,
        loader: 'html-loader'
      }
    ],
  },
};
