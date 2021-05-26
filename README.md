
# Parasaurolophus: Music Recommender
A Machine Learning Project | UBC CPEN 291 team project 

## Project Desctiption
Parasaurolophus, named after the dinosaur known for its unique sound, is an app that gives music recommendations to users. The application takes an input wav file and uses a genre classifier’s prediction to recommend other music from the same genre. Eight music genres are currently supported, namely: Blues,Country, Electronic, Folk, Jazz, Latin, Rock, and Rap music. Finally, the recommendation is automatically copied to the user’s clipboard for convenience. 

## Project Demo

https://user-images.githubusercontent.com/36906268/119421956-c0d12800-bcb4-11eb-992c-c8267e52f015.mp4

## Developing the Machine Learning Component
- Data collection
     - Spectrogram extraction from YouTube audio samples
     - Automation of spectrogram extraction and storage process
- Model training and testing
    - Experimented with various training parameters, such as batch size, and learning rate to optimize for fast training and high genre classification accuracy.
    - Experimented with various data parameters, including number of genres, and number of samples per genre to optimize for high genre classification accuracy.
- Learned the framework Ensemble-Pytorch for further improvement to genre classification accuracy
    - Now, we can easily experiment with different kinds of machine learning ensembles to improve the accuracy of our genre classifier.

## Further Details

For a more details on data flow and modules, see our final report:
- https://github.com/Aswin-SaiSubramanian/Music-Recommender/blob/main/CPEN%20291%20Project%20Final%20Report.pdf

Details about the development of this project and design decision can be found in our milestone reports:
- Milestone 1 | https://github.com/Aswin-SaiSubramanian/Music-Recommender/blob/main/reports/M1/Team%20Dilphosaurus%20-%20Milestone%201%20Report.pdf
- Milestone 2 | https://github.com/Aswin-SaiSubramanian/Music-Recommender/blob/main/reports/M2/Team%20Dilphosaurus%20-%20Milestone%202%20Report.pdf
- Milestone 3 | https://github.com/Aswin-SaiSubramanian/Music-Recommender/blob/main/reports/M3/Team%20Dilphosaurus%20-%20Milestone%203%20Report.pdf
- Milestone 4 | https://github.com/Aswin-SaiSubramanian/Music-Recommender/blob/main/reports/M4/Team%20Dilphosaurus%20-%20Milestone%204%20Report.pdf

<!-- 
## Highlights

- Data Flow
    - Spectrogram extraction
    - Preparing model input
    - Interpreting model output -->










