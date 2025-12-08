# Lecture notes generator

This project was made for applying to Metropolia AI project student assistant role. The project is a small Flask app, that helps students and teachers generate written lecture notations from audio or video recording.

The app will take the uploaded video or audio file and generate a written lecture notes -style summary of the content. The user can then save the text output, and use it as needed. 

## Features

- Upload video or audio files via a simple Flask web interface.
- Automatic audio extraction from video files (MP4, MKV, MOV, AVI) using Ffmpeg tool.
- Speech transcription using OpenAI Whisper API.
- Text cleaning and summarization using GPT (concurrent processing for speed).
- Produces structured lecture notes with main points, headings, and bullet lists.

## Usage

1. Clone the repository and install dependencies.
2. Set your OpenAI API key in .env.
3. Run the Flask app.
4. Upload a video or audio file to generate lecture notes.

## Development choices

The main focus in development was to create a fast and reliable tool, that works with any kind of material. This efficiency optimization led to the chosen technologies.

Audio extraction is done by Ffmpeg command line tool. The tool will extract the audio in lowest possible quality that Whisper transcription can work with. 
I chose to use the API version of Whisper instead of local model to save on processing power and time, but a local model could have been used as well. In my testing this increased the process runtime, and as OpenAi api was already being used, it was a natural choice.
The text processing is done via OpenAI ChatGPT 5 Nano model via the api. Nano is the smallest and most cost efficient model in the api, and it excels in text cleaning and summarization.
The output from whisper transcription is always messy, so the text is first cleaned up before summarization. This is done simultaneously for multiple chunks with threading, again to save on processing time. 
The individual chunks are cleaned and summarized, and then finally all summaries are combined into a single summary for the user.

## Testing

The model was tested with video and audio files with length up to one hour. With longer files the processing time increased, but even with the longest tried video of one hour, the app took 10 minutes to output the summary. This was considerably faster with shorter files. 

## Future improvements

Main improvements would be to use local models instead of the api. Using the local ChatGpt and Whisper models would improve cost-efficiency, and maintain data security.
Another improvement I will be adding to the app is the ability to get summaries just from a Youtube video url. This would be useful in understanding new subjects faster, or generate new lecture materials quickly.
The app could also be upgraded to accept also lecture materials in other formats, such as .pdf or .pp to generate summaries purely from lecture slides and materials.

The final app could be used as a tool on its own, or it could be integrated into a pipeline, where the app would provide metadata for files that are uploaded into a system. 
This would help finding videos and lectures on specific topics, as it would also make searching on subjects easier.

The app will help students to get cohesive notes even if they are unable to attend a class, and will help teachers improve lecture materials and provide students with easy summaries on lecture subjects.
