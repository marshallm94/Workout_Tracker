import { useSpeechRecognition } from "@/hooks/Main";

export const Main = () => {
  const {
    text,
    confidence,
    isListening,
    startListening,
    stopListening,
    hasRecognitionSupport,
  } = useSpeechRecognition();

  return (
    <div>
      {hasRecognitionSupport ? (
        <>
          <div>
            <button onClick={startListening}>
              Click me to start listening
            </button>
            <button onClick={stopListening}>Click me to stop listening</button>
          </div>
          {isListening ? <div>Your browser is listening to you</div> : null}
          {!isListening && text.length > 0 ? (
            <div>
              <p>Your speech is: {text}</p>
              <p>with confidence: {confidence}</p>
            </div>
          ) : (
            <div></div>
          )}
        </>
      ) : (
        <h1>Your browser doesn't support speech recognition</h1>
      )}
    </div>
  );
};
