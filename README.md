# ICSIMA Base Code — ISS Telemetry and Status Scripts

**Status: public-release draft; source-to-paper alignment needs confirmation.**

This repository is a cleaned packaging of the Python scripts supplied in the
`ICSIMA_Codes-main` archive. The included scripts acquire International Space
Station (ISS) coordinates from the Open Notify endpoint, append coordinates to
a local CSV, report whether a named process is running, and send status/file-size
updates to a Google Apps Script endpoint.

## Important scope clarification

The supplied research paper, *Feature-Augmented YOLO for Space Debris Detection
and Immediate Trajectory Prediction*, describes YOLO object detection,
MobileNetV2 image features, bounding-box features, and trajectory regression.
Those model-training and evaluation components are **not present in the
top-level Python scripts in the supplied ZIP**. The ZIP instead contains ISS
telemetry/status automation scripts and a nested `GitAction.zip` archive.

Do not describe this repository alone as implementing the paper's YOLO detection
or trajectory-prediction methodology until the missing source code is located
and verified. This repository is kept separate from the image-based extension
to preserve the distinction between supplied base scripts and subsequent work.

## Included scripts

- `Acquire_ISS_Data.py` — polls the ISS position endpoint and appends timestamp,
  longitude, and latitude to `iss_location.csv`.
- `ISS_Acquire_Transmit.py` — polls ISS position and sends it to a configured
  Apps Script endpoint.
- `UpdateSimple.py`, `UpdateSimpleLoop.py` — sends simple run-status updates.
- `UpdateSimpleLoopWProcess.py`, `UpdateSimpleLoopWFilesize.py` — checks a
  process name and/or local CSV file size, then reports status.
- `GetProcessStatus.py` — checks for a process whose command line contains
  `AcquireData.py`. Adjust this target to the actual script name if needed.
- `UpdateSimpleLoop.py` and related scripts are legacy examples; they have not
  been independently validated end-to-end.

## Setup

Python 3.10+ is a reasonable starting point; compatibility has not been tested
across all platforms.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\\Scripts\\activate`.

## Configuration and safety

Scripts that send data to Google Apps Script use the environment variable
`GOOGLE_APPS_SCRIPT_URL` instead of embedding a deployment URL in source code.
Set it only to an endpoint you own or are authorized to use. Do not commit
private deployment URLs, tokens, credentials, or personal data.

```bash
export GOOGLE_APPS_SCRIPT_URL="https://script.google.com/macros/s/YOUR_AUTHORIZED_DEPLOYMENT_ID/exec"
```

Some legacy scripts use query parameters to transmit run status, coordinates,
or file size. Review the destination and data being sent before running them.
The polling scripts run continuously until stopped with Ctrl+C. Use a timeout
and test against a non-sensitive endpoint first.

## Research-paper relationship

The accompanying paper describes an image-based detection and trajectory
prediction framework. The supplied ZIP does not provide enough source code to
reproduce the paper's reported detection or regression metrics. Dataset details,
training scripts, checkpoints, exact evaluation code, and permissions should be
verified before claiming reproducibility.

## Public-release checklist

- [ ] Confirm authorship/permission to publish every included script.
- [ ] Confirm the supplied ZIP's scripts are the intended base implementation
      for the paper; locate the model code if it exists elsewhere.
- [ ] Review the Google Apps Script deployment and authorization before use.
- [ ] Test scripts with an authorized endpoint and document observed behavior.
- [ ] Add verified dataset/source citations if relevant.
- [ ] Add a project license only after confirming code ownership and rights.

## License

No license is included. Reuse permissions are not asserted by this draft.
