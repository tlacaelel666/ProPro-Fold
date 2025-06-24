{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9631dd89",
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "execution": {
     "iopub.execute_input": "2025-06-24T07:56:19.346516Z",
     "iopub.status.busy": "2025-06-24T07:56:19.345690Z",
     "iopub.status.idle": "2025-06-24T07:56:20.915134Z",
     "shell.execute_reply": "2025-06-24T07:56:20.914122Z"
    },
    "papermill": {
     "duration": 1.573816,
     "end_time": "2025-06-24T07:56:20.916714",
     "exception": false,
     "start_time": "2025-06-24T07:56:19.342898",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/kaggle/input/protein/PGP_ Descripcin Tcnica Concisa.pdf\n",
      "/kaggle/input/protein/NLP_SENTIMENT_ANALYSIS_USING_RoBERTa.pdf\n",
      "/kaggle/input/protein/foldingPQ.pdf\n",
      "/kaggle/input/protein/Python code for Artificial Intelligence.pdf\n",
      "/kaggle/input/protein/NLP_Transformer_Based_Models_Used_For_sentiment_Analysis.pdf\n",
      "/kaggle/input/protein/The_LSTM_Layer.pdf\n",
      "/kaggle/input/protein/PostPolGraQ.docx\n",
      "/kaggle/input/protein/Neural_Network_And_Deep_Learning.pdf\n",
      "/kaggle/input/protein/marco_matematico.md\n",
      "/kaggle/input/protein/Optimize LLM costs.pdf\n",
      "/kaggle/input/protein/Types Of Vector Search.pdf\n",
      "/kaggle/input/protein/Distance Metrics in Machine Learning with Python.pdf\n",
      "/kaggle/input/protein/LLM para regresin.pdf\n",
      "/kaggle/input/protein/quantum-protein-analyzer/index.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/App.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/constants.ts\n",
      "/kaggle/input/protein/quantum-protein-analyzer/.gitignore\n",
      "/kaggle/input/protein/quantum-protein-analyzer/README.md\n",
      "/kaggle/input/protein/quantum-protein-analyzer/metadata.json\n",
      "/kaggle/input/protein/quantum-protein-analyzer/.env.local\n",
      "/kaggle/input/protein/quantum-protein-analyzer/types.ts\n",
      "/kaggle/input/protein/quantum-protein-analyzer/vite.config.ts\n",
      "/kaggle/input/protein/quantum-protein-analyzer/tsconfig.json\n",
      "/kaggle/input/protein/quantum-protein-analyzer/index.html\n",
      "/kaggle/input/protein/quantum-protein-analyzer/package.json\n",
      "/kaggle/input/protein/quantum-protein-analyzer/services/pgpTheoryService.ts\n",
      "/kaggle/input/protein/quantum-protein-analyzer/services/quantumSimulatorService.ts\n",
      "/kaggle/input/protein/quantum-protein-analyzer/services/excitationDynamicsService.ts\n",
      "/kaggle/input/protein/quantum-protein-analyzer/services/dvmSimulationService.ts\n",
      "/kaggle/input/protein/quantum-protein-analyzer/services/geminiService.ts\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/GeminiInteraction.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/Icons.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/AppHeader.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/MainMenuView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/ViewContainer.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/Notification.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/MainMenuView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/SimulateDynamicsView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/CreateHamiltonianView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/SimulateExcitationDynamicsView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/CreateCircuitView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/AnalyzeOperatorView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/VisualizeCircuitView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/GeminiGeneralInsightsView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/VisualizeResultsView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/HistoryView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/pgp/PgpSusceptibilityView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/pgp/PgpMassificationView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/pgp/PgpMaxwellGinzburgView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/pgp/PgpLaminarFlowView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/pgp/PgpMasterEquationView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/pgp/PgpLagrangianView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/pgp/PgpResponseFieldView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/dvm/DvmSetupView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/views/dvm/DvmVisualizationView.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/common/Input.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/common/Button.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/common/Modal.tsx\n",
      "/kaggle/input/protein/quantum-protein-analyzer/components/common/Card.tsx\n"
     ]
    }
   ],
   "source": [
    "# This Python 3 environment comes with many helpful analytics libraries installed\n",
    "# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n",
    "# For example, here's several helpful packages to load\n",
    "\n",
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "\n",
    "# Input data files are available in the read-only \"../input/\" directory\n",
    "# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n",
    "\n",
    "import os\n",
    "for dirname, _, filenames in os.walk('/kaggle/input'):\n",
    "    for filename in filenames:\n",
    "        print(os.path.join(dirname, filename))\n",
    "\n",
    "# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n",
    "# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session"
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "datasetId": 7727987,
     "sourceId": 12263776,
     "sourceType": "datasetVersion"
    }
   ],
   "dockerImageVersionId": 31040,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 6.118048,
   "end_time": "2025-06-24T07:56:21.336451",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2025-06-24T07:56:15.218403",
   "version": "2.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
