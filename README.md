# Wedding Website
We built this site to let our friends and guests RSVP online. It was a COVID wedding, so we needed to communicate how they should tune in, how we would do photo taking, etc. We eventually hosted it on GCP using the trial credits.

**Things to note**:
<br>
- The /static/images folder is empty, but anyone can populate them with the filenames *'gallery_01.jpg'*, *'gallery_02.jpg'*... *gallery_27.jpg* easily.
- config.ini is where the credentials were kept.


To run:
1. git clone https://github.com/LeongBryan/weddingwebsite.git
2. pip install -r requirements.txt
3. waitress-serve api:app


This is what it can look like:
![alt-text](https://github.com/LeongBryan/weddingwebsite/blob/main/wedding-site.gif)
