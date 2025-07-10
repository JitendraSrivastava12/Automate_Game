<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🎮 Automated Game Control (Hand Gesture Based)</title>
</head>
<body>

  <h1>🎮 Automated Game Control Using Hand Gestures</h1>
  <p>
    A gesture-based control system that lets you play games using hand movements! The system leverages computer vision to detect fingers in real time and maps them to game actions — all without touching a keyboard or controller.
  </p>

  <h3>🔗 Link to Demo App</h3>
  <p><a href="https://your-game-control-app-link">Launch the Game Controller</a></p>

  <h3>🖐️ Gesture-to-Action Mapping</h3>
  <ul>
    <li>☝️ 1 Finger: Move Left</li>
    <li>✌️ 2 Fingers: Move Right</li>
    <li>🤟 3 Fingers: Move Down</li>
    <li>🖖 4 Fingers: Jump</li>
  </ul>

  <h3>🚀 Features</h3>
  <ul>
    <li>📹 Real-time hand landmark detection using webcam</li>
    <li>🧠 Gesture classification using number of fingers</li>
    <li>🎮 Automated keypress triggers for game events</li>
    <li>🔧 Customizable gesture-action mapping</li>
    <li>📱 Runs on web using Streamlit or integrates with games via Python</li>
  </ul>

  <h3>📦 Tech Stack</h3>
  <h4>Frontend:</h4>
  <ul>
    <li>Streamlit</li>
    <li>streamlit-webrtc</li>
  </ul>
  <h4>Backend:</h4>
  <ul>
    <li>OpenCV</li>
    <li>cvzone</li>
    <li>MediaPipe</li>
    <li>PyAutoGUI (for triggering keyboard inputs)</li>
  </ul>
  <h4>Language:</h4>
  <ul>
    <li>Python</li>
  </ul>

  <h3>🔧 Installation</h3>
  <pre><code>
git clone https://github.com/YOUR_USERNAME/game-control-gesture.git
cd game-control-gesture
pip install -r requirements.txt
  </code></pre>

  <h3>▶️ Run the App</h3>
  <pre><code>streamlit run app.py</code></pre>

  <h3>🛠 Deployment</h3>
  <ul>
    <li>Compatible with Streamlit Cloud, Render, etc.</li>
    <li>Ensure webcam permissions are enabled</li>
    <li>Use Chrome or Firefox for best performance</li>
  </ul>

  <h3>❗ Known Issues</h3>
  <ul>
    <li>Lighting conditions affect gesture detection accuracy</li>
    <li>Latency may occur on low-spec devices</li>
    <li>Some games may block simulated keypress input</li>
  </ul>

  <h3>🙌 Acknowledgements</h3>
  <ul>
    <li>cvzone</li>
    <li>OpenCV</li>
    <li>MediaPipe</li>
    <li>PyAutoGUI</li>
    <li>Streamlit</li>
  </ul>

  <h3>📄 License</h3>
  <p>This project is licensed under the MIT License – see the LICENSE file for details.</p>

</body>
</html>
