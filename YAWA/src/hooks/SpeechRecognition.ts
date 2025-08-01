import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

export function RecordSpeech() {
  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition,
  } = useSpeechRecognition();

  if (!browserSupportsSpeechRecognition) {
    console.log("browser does not support speech");
  } else if (browserSupportsSpeechRecognition) {
    console.log("browser does support speech");
  }

  function startListening() {
    SpeechRecognition.startListening();
  }
  function stopListenting() {
    SpeechRecognition.stopListening();
  }
  return (startListening, stopListenting, transcript, listening);
}
