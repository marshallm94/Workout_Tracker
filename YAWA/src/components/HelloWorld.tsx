import { LogSomeShit } from "@/hooks/AddContact";
import { RecordSpeech } from "@/hooks/SpeechRecognition";
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

export function HelloWorld() {
  return <button onClick={LogSomeShit}>Click Me</button>;
}

export const Dictaphone = () => {
  const { startListening, stopListening, transcript, listening } =
    RecordSpeech();

  return (
    <div>
      <p>Listening: {listening ? "Yes" : "No"}</p>
      <button onClick={startListening}>Start Listening</button>
      <button onClick={stopListening}>Stop Listening</button>
      <p>Transcript</p>
      <pre>{transcript}</pre>
    </div>
  );
};
