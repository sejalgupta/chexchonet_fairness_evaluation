# chexchonet_fairness_evaluation

This is code for the paper "Gold" Standard in Question: Evaluation of the Fairness of Classifiers Trained on Gold-Standard Chest X-ray Datasets by Sejal Gupta for the class 6.S977. 

To train the model, run `conda activate chexchonet & python -m visdom.server & python -m run -m dense_base_with_demo -ci 0 -vi CHEXONET_RUN_9 -c ./train_configs/train_config_9.yaml`

To test the model, run `conda activate chexchonet & python -m run_test_set -ckpt ./model_checkpoint/chexnet_9.pth.tar -ts ./best_models/CHEXONET_RUN_9/test_set_settings.pth -fname test_results_9.csv`

To evaluate the model, run the following:
1. Run `calculate_thresholds.ipynb`
2. Run `tpr_analysis.py`
3. Run `plot.ipnyb`
4. Run 1 and 2 for each of the runs in the respective results folders
5. Run `confidence.ipynb`
6. Run `second_confidence.ipynb`
