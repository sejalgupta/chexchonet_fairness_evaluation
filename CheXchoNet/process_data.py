from src.train.helpers import *
import pandas as pd

df_train, df_eval, df_test = split_train_eval_test("../physionet.org/files/chexchonet/1.0.0/metadata.csv", 42)
df_train, df_eval, df_test = split_train_eval_test("../physionet.org/files/chexchonet/1.0.0/metadata.csv", 9)
df_train, df_eval, df_test = split_train_eval_test("../physionet.org/files/chexchonet/1.0.0/metadata.csv", 35)
df_train, df_eval, df_test = split_train_eval_test("../physionet.org/files/chexchonet/1.0.0/metadata.csv", 21)
df_train, df_eval, df_test = split_train_eval_test("../physionet.org/files/chexchonet/1.0.0/metadata.csv", 25)