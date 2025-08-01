import { useState, useEffect } from "react";

let recognition: any = null;
if ("webkitSpeechRecognition" in window) {
  console.log("Speech recognition available");
  recognition = new webkitSpeechRecognition();
  recognition.continuous = true;
  recognition.lang = "en-US";
} else if (!("webkitSpeechRecognition" in window)) {
  console.log("Speech recognition not available");
}

export const useSpeechRecognition = () => {
  const [text, setText] = useState("");
  const [confidence, setConfidence] = useState(0);
  const [isListening, setIsListening] = useState(false);

  useEffect(() => {
    if (!recognition) {
      return;
    }

    recognition.onresult = (event: SpeechRecognitionEvent) => {
      setText(event.results[0][0].transcript);
      setConfidence(event.results[0][0].confidence);
      recognition.stop();
      setIsListening(false);
    };

    recognition.onerror = (event: any) => {
      console.error("Speech recognition error:", event.error);
    };
  }, []);

  const startListening = () => {
    setText("");
    setIsListening(true);
    recognition.start();
  };

  const stopListening = () => {
    setIsListening(false);
    recognition.stop();
  };
  console.log(text);
  console.log(confidence);

  return {
    text,
    confidence,
    isListening,
    startListening,
    stopListening,
    hasRecognitionSupport: !!recognition,
  };
};
