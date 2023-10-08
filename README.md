# Social_Video_Tutorial
A tutorial about acquiring and analysing videos of social behaviour.

- What is behaviour?
- What is an image?

How do you extract (social) behaviour from an image (or sequence of images, i.e. video)?

## Background
We will use Python to open, process, and save images/videos of animals engaged in social interactions.

You will need to install Visual Studio Code and the Pyton extension. You can follw the installation instructions here:
https://code.visualstudio.com/docs/python/python-tutorial

## Setup Python

- Create a virtual environment

```bash
mkdir _tmp
cd _tmp
python -m venv SVT
source SVT/bin/activate
```

- Install useful Python libraries

```bash
pip install numpy imageio[ffmpeg] scikit-image 
```

### Examples

1. Load image, threshold, and save result


## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />The entire LastBlackBox repository and website is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
