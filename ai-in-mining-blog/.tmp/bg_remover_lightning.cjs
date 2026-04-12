const Jimp = require('jimp');

const imgPath = '/home/jgrah/Blog_EI_Safety/ai-in-mining-blog/src/assets/symbol-lightning.png';

Jimp.read(imgPath).then(image => {
    const targetR = image.bitmap.data[0];
    const targetG = image.bitmap.data[1];
    const targetB = image.bitmap.data[2];
    
    console.log(`Keying out background color rgb(${targetR},${targetG},${targetB})`);

    image.scan(0, 0, image.bitmap.width, image.bitmap.height, function (x, y, idx) {
        var red   = this.bitmap.data[idx + 0];
        var green = this.bitmap.data[idx + 1];
        var blue  = this.bitmap.data[idx + 2];

        if (Math.abs(red - targetR) < 15 && Math.abs(green - targetG) < 15 && Math.abs(blue - targetB) < 15) {
            this.bitmap.data[idx + 3] = 0; // Transparent
        }
    });
    image.write(imgPath, () => {
        console.log("Done processing symbol-lightning.png");
    });
}).catch(console.error);
