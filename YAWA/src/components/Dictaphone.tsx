import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

export const Dictaphone = () => {
  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition,
  } = useSpeechRecognition();

  if (!browserSupportsSpeechRecognition) {
    return <span>Browser doesn't support speech recognition.</span>;
  }

  const startListeningWrapper = () => {
    SpeechRecognition.startListening({
      continuous: true,
    });
  };

  const stopListeningWrapper = () => {
    SpeechRecognition.stopListening();
    console.log(transcript);
  };

  return (
    <div>
      <p>Microphone: {listening ? "on" : "off"}</p>
      <button onClick={startListeningWrapper}>Start</button>
      <button onClick={stopListeningWrapper}>Stop</button>
      <button onClick={resetTranscript}>Reset</button>
      <p>{transcript}</p>
    </div>
  );
};
