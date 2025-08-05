> 📝 Click on the language section to expand / 言語をクリックして展開

# Wan 2.1 / 2.2

## Overview / 概要

This is an unofficial training and inference script for [Wan2.1](https://github.com/Wan-Video/Wan2.1) and Wan2.2 models. The features are as follows.

- fp8 support and memory reduction by block swap: Inference of a 720x1280x81frames videos with 24GB VRAM, training with 720x1280 images with 24GB VRAM
- Inference without installing Flash attention (using PyTorch's scaled dot product attention)
- Supports xformers and Sage attention
- **Wan2.2 support**: Enhanced models with improved quality and dual-checkpoint architecture

This feature is experimental.

### Key Differences: Wan2.1 vs Wan2.2

| Feature | Wan2.1 | Wan2.2 |
|---------|---------|---------|
| **Architecture** | Single checkpoint | Dual-checkpoint (low-noise + high-noise) |
| **Model Tasks** | `t2v-14B`, `i2v-14B`, `t2v-1.3B`, etc. | `t2v-A14B`, `i2v-A14B` |
| **Default Steps** | 20 steps | 40 steps |
| **Flow Shift** | 5.0 (most), 3.0 (I2V 480p) | 12.0 (T2V), 5.0 (I2V) |
| **Guidance Scale** | 5.0 | (3.0, 4.0) for T2V, (3.5, 3.5) for I2V |
| **Quality** | Good | Enhanced quality with dual-checkpoint |
| **Command Line** | `--dit model.safetensors` | `--dit low_noise.safetensors --dit_high_noise high_noise.safetensors` |

**Wan2.2 models provide improved quality through their dual-checkpoint architecture but require more careful setup.**

<details>
<summary>日本語</summary>
[Wan2.1](https://github.com/Wan-Video/Wan2.1) およびWan2.2モデルの非公式の学習および推論スクリプトです。

以下の特徴があります。

- fp8対応およびblock swapによる省メモリ化：720x1280x81framesの動画を24GB VRAMで推論可能、720x1280の画像での学習が24GB VRAMで可能
- Flash attentionのインストールなしでの実行（PyTorchのscaled dot product attentionを使用）
- xformersおよびSage attention対応
- **Wan2.2サポート**: 品質向上とデュアルチェックポイントアーキテクチャを持つ拡張モデル

この機能は実験的なものです。

### 主な違い: Wan2.1 vs Wan2.2

| 機能 | Wan2.1 | Wan2.2 |
|------|---------|---------|
| **アーキテクチャ** | シングルチェックポイント | デュアルチェックポイント（低ノイズ+高ノイズ） |
| **モデルタスク** | `t2v-14B`, `i2v-14B`, `t2v-1.3B` 等 | `t2v-A14B`, `i2v-A14B` |
| **デフォルトステップ数** | 20ステップ | 40ステップ |
| **フローシフト** | 5.0（ほとんど）、3.0（I2V 480p） | 12.0（T2V）、5.0（I2V） |
| **ガイダンススケール** | 5.0 | T2V: (3.0, 4.0)、I2V: (3.5, 3.5) |
| **品質** | 良好 | デュアルチェックポイントにより品質向上 |
| **コマンドライン** | `--dit model.safetensors` | `--dit low_noise.safetensors --dit_high_noise high_noise.safetensors` |

**Wan2.2モデルはデュアルチェックポイントアーキテクチャにより品質が向上していますが、より注意深いセットアップが必要です。**
</details>

## Download the model / モデルのダウンロード

### Wan2.1 Models

Download the T5 `models_t5_umt5-xxl-enc-bf16.pth` and CLIP `models_clip_open-clip-xlm-roberta-large-vit-huge-14.pth` from the following page: https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P/tree/main

Download the VAE from the above page `Wan2.1_VAE.pth` or download `split_files/vae/wan_2.1_vae.safetensors` from the following page: https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/vae

Download the DiT weights from the following page: https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models

Wan2.1 Fun Control model weights can be downloaded from [here](https://huggingface.co/alibaba-pai/Wan2.1-Fun-14B-Control). Navigate to each weight page and download. The Fun Control model seems to support not only T2V but also I2V tasks.

### Wan2.2 Models

**Wan2.2 14B models use a dual-checkpoint architecture** with separate low-noise and high-noise models for improved quality.

For **Wan2.2 14B models** (`t2v-A14B` and `i2v-A14B`), you need to download:
- **T5 and VAE**: Same as Wan2.1 (use the same files from above)
- **DiT Models**: Two separate checkpoint files:
  - Low-noise model (main model)
  - High-noise model (companion model for high-noise denoising)

**Note**: Official Wan2.2 model download links are not yet available. Please check the official Wan repositories for model release announcements.

Please select the appropriate weights according to T2V, I2V, resolution, model size, etc. 

`fp16` and `bf16` models can be used, and `fp8_e4m3fn` models can be used if `--fp8` (or `--fp8_base`) is specified without specifying `--fp8_scaled`. **Please note that `fp8_scaled` models are not supported even with `--fp8_scaled`.**

(Thanks to Comfy-Org for providing the repackaged weights.)

### Model support matrix / モデルサポートマトリックス

* columns: training dtype (行：学習時のデータ型)
* rows: model dtype (列：モデルのデータ型)

| model \ training |bf16|fp16|--fp8_base|--fp8base & --fp8_scaled|
|--|--|--|--|--|
|bf16|✓|--|✓|✓|
|fp16|--|✓|✓|✓|
|fp8_e4m3fn|--|--|✓|--|
|fp8_scaled|--|--|--|--|

<details>
<summary>日本語</summary>

### Wan2.1モデル

T5 `models_t5_umt5-xxl-enc-bf16.pth` およびCLIP `models_clip_open-clip-xlm-roberta-large-vit-huge-14.pth` を、次のページからダウンロードしてください：https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P/tree/main

VAEは上のページから `Wan2.1_VAE.pth` をダウンロードするか、次のページから `split_files/vae/wan_2.1_vae.safetensors` をダウンロードしてください：https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/vae

DiTの重みを次のページからダウンロードしてください：https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models

Wan2.1 Fun Controlモデルの重みは、[こちら](https://huggingface.co/alibaba-pai/Wan2.1-Fun-14B-Control)から、それぞれの重みのページに遷移し、ダウンロードしてください。Fun ControlモデルはT2VだけでなくI2Vタスクにも対応しているようです。

### Wan2.2モデル

**Wan2.2 14Bモデルはデュアルチェックポイントアーキテクチャ**を使用し、品質向上のために低ノイズモデルと高ノイズモデルが分離されています。

**Wan2.2 14Bモデル**（`t2v-A14B`および`i2v-A14B`）については、以下をダウンロードする必要があります：
- **T5とVAE**: Wan2.1と同じ（上記のファイルと同じものを使用）
- **DiTモデル**: 2つの独立したチェックポイントファイル：
  - 低ノイズモデル（メインモデル）
  - 高ノイズモデル（高ノイズデノイジング用コンパニオンモデル）

**注意**: 公式のWan2.2モデルダウンロードリンクはまだ利用できません。モデルのリリース発表については、公式Wanリポジトリを確認してください。

T2VやI2V、解像度、モデルサイズなどにより適切な重みを選択してください。

`fp16` および `bf16` モデルを使用できます。また、`--fp8` （または`--fp8_base`）を指定し`--fp8_scaled`を指定をしないときには `fp8_e4m3fn` モデルを使用できます。**`fp8_scaled` モデルはいずれの場合もサポートされていませんのでご注意ください。**

（repackaged版の重みを提供してくださっているComfy-Orgに感謝いたします。）
</details>

## Pre-caching / 事前キャッシュ

### Latent Pre-caching

Latent pre-caching is almost the same as in HunyuanVideo. Create the cache using the following command:

```bash
python src/musubi_tuner/wan_cache_latents.py --dataset_config path/to/toml --vae path/to/wan_2.1_vae.safetensors
```

If you train I2V models, add `--clip path/to/models_clip_open-clip-xlm-roberta-large-vit-huge-14.pth` to specify the CLIP model. If not specified, the training will raise an error.

If you're running low on VRAM, specify `--vae_cache_cpu` to use the CPU for the VAE internal cache, which will reduce VRAM usage somewhat.

The control video settings are required for training the Fun-Control model. Please refer to [Dataset Settings](/src/musubi_tuner/dataset/dataset_config.md#sample-for-video-dataset-with-control-images) for details.

<details>
<summary>日本語</summary>
latentの事前キャッシングはHunyuanVideoとほぼ同じです。上のコマンド例を使用してキャッシュを作成してください。

I2Vモデルを学習する場合は、`--clip path/to/models_clip_open-clip-xlm-roberta-large-vit-huge-14.pth` を追加してCLIPモデルを指定してください。指定しないと学習時にエラーが発生します。

VRAMが不足している場合は、`--vae_cache_cpu` を指定するとVAEの内部キャッシュにCPUを使うことで、使用VRAMを多少削減できます。

Fun-Controlモデルを学習する場合は、制御用動画の設定が必要です。[データセット設定](/src/musubi_tuner/dataset/dataset_config.md#sample-for-video-dataset-with-control-images)を参照してください。
</details>

### Text Encoder Output Pre-caching

Text encoder output pre-caching is also almost the same as in HunyuanVideo. Create the cache using the following command:

```bash
python src/musubi_tuner/wan_cache_text_encoder_outputs.py --dataset_config path/to/toml  --t5 path/to/models_t5_umt5-xxl-enc-bf16.pth --batch_size 16 
```

Adjust `--batch_size` according to your available VRAM.

For systems with limited VRAM (less than ~16GB), use `--fp8_t5` to run the T5 in fp8 mode.

<details>
<summary>日本語</summary>
テキストエンコーダ出力の事前キャッシングもHunyuanVideoとほぼ同じです。上のコマンド例を使用してキャッシュを作成してください。

使用可能なVRAMに合わせて `--batch_size` を調整してください。

VRAMが限られているシステム（約16GB未満）の場合は、T5をfp8モードで実行するために `--fp8_t5` を使用してください。
</details>

## Training / 学習

### Training

Start training using the following command (input as a single line):

```bash
accelerate launch --num_cpu_threads_per_process 1 --mixed_precision bf16 src/musubi_tuner/wan_train_network.py 
    --task t2v-1.3B 
    --dit path/to/wan2.1_xxx_bf16.safetensors 
    --dataset_config path/to/toml --sdpa --mixed_precision bf16 --fp8_base 
    --optimizer_type adamw8bit --learning_rate 2e-4 --gradient_checkpointing 
    --max_data_loader_n_workers 2 --persistent_data_loader_workers 
    --network_module networks.lora_wan --network_dim 32 
    --timestep_sampling shift --discrete_flow_shift 3.0 
    --max_train_epochs 16 --save_every_n_epochs 1 --seed 42
    --output_dir path/to/output_dir --output_name name-of-lora
```
The above is an example. The appropriate values for `timestep_sampling` and `discrete_flow_shift` need to be determined by experimentation.

For additional options, use `python src/musubi_tuner/wan_train_network.py --help` (note that many options are unverified).

`--task` is one of:
- **Wan2.1 models**: `t2v-1.3B`, `t2v-14B`, `i2v-14B`, `t2i-14B` (official models)
- **Wan2.1 Fun Control models**: `t2v-1.3B-FC`, `t2v-14B-FC`, `i2v-14B-FC`
- **Wan2.2 models**: `t2v-A14B`, `i2v-A14B` (enhanced 14B models with dual-checkpoint architecture)

Specify the DiT weights for the task with `--dit`. For Wan2.2 models, you also need to specify `--dit_high_noise` for the high-noise model checkpoint.

Don't forget to specify `--network_module networks.lora_wan`.

Other options are mostly the same as `hv_train_network.py`.

Use `convert_lora.py` for converting the LoRA weights after training, as in HunyuanVideo.

<details>
<summary>日本語</summary>
`timestep_sampling`や`discrete_flow_shift`は一例です。どのような値が適切かは実験が必要です。

その他のオプションについては `python src/musubi_tuner/wan_train_network.py --help` を使用してください（多くのオプションは未検証です）。

`--task` には以下のいずれかを指定します：
- **Wan2.1モデル**: `t2v-1.3B`, `t2v-14B`, `i2v-14B`, `t2i-14B` （公式モデル）
- **Wan2.1 Fun Controlモデル**: `t2v-1.3B-FC`, `t2v-14B-FC`, `i2v-14B-FC`
- **Wan2.2モデル**: `t2v-A14B`, `i2v-A14B` （デュアルチェックポイントアーキテクチャを持つ拡張14Bモデル）

`--dit`に、taskに応じたDiTの重みを指定してください。Wan2.2モデルの場合は、高ノイズモデルチェックポイント用に`--dit_high_noise`も指定する必要があります。

 `--network_module` に `networks.lora_wan` を指定することを忘れないでください。

その他のオプションは、ほぼ`hv_train_network.py`と同様です。

学習後のLoRAの重みの変換は、HunyuanVideoと同様に`convert_lora.py`を使用してください。
</details>

### Command line options for training with sampling / サンプル画像生成に関連する学習時のコマンドラインオプション

Example of command line options for training with sampling / 記述例:  

```bash
--vae path/to/wan_2.1_vae.safetensors 
--t5 path/to/models_t5_umt5-xxl-enc-bf16.pth 
--sample_prompts /path/to/prompt_file.txt 
--sample_every_n_epochs 1 --sample_every_n_steps 1000 -- sample_at_first
```
Each option is the same as when generating images or as HunyuanVideo. Please refer to [here](/docs/sampling_during_training.md) for details.

If you train I2V models, add `--clip path/to/models_clip_open-clip-xlm-roberta-large-vit-huge-14.pth` to specify the CLIP model. 

You can specify the initial image, the negative prompt and the control video (for Wan2.1-Fun-Control) in the prompt file. Please refer to [here](/docs/sampling_during_training.md#prompt-file--プロンプトファイル).

<details>
<summary>日本語</summary>
各オプションは推論時、およびHunyuanVideoの場合と同様です。[こちら](/docs/sampling_during_training.md)を参照してください。

I2Vモデルを学習する場合は、`--clip path/to/models_clip_open-clip-xlm-roberta-large-vit-huge-14.pth` を追加してCLIPモデルを指定してください。

プロンプトファイルで、初期画像やネガティブプロンプト、制御動画（Wan2.1-Fun-Control用）等を指定できます。[こちら](/docs/sampling_during_training.md#prompt-file--プロンプトファイル)を参照してください。
</details>


## Inference / 推論

### Inference Options Comparison / 推論オプション比較

#### Speed Comparison (Faster → Slower) / 速度比較（速い→遅い）
*Note: Results may vary depending on GPU type*

fp8_fast > bf16/fp16 (no block swap) > fp8 > fp8_scaled > bf16/fp16 (block swap)

#### Quality Comparison (Higher → Lower) / 品質比較（高→低）

bf16/fp16 > fp8_scaled > fp8 >> fp8_fast

### T2V Inference / T2V推論

#### Wan2.1 T2V Inference

The following is an example of Wan2.1 T2V inference (input as a single line):

```bash
python src/musubi_tuner/wan_generate_video.py --fp8 --task t2v-1.3B --video_size  832 480 --video_length 81 --infer_steps 20 
--prompt "prompt for the video" --save_path path/to/save.mp4 --output_type both 
--dit path/to/wan2.1_t2v_1.3B_bf16_etc.safetensors --vae path/to/wan_2.1_vae.safetensors 
--t5 path/to/models_t5_umt5-xxl-enc-bf16.pth 
--attn_mode torch
```

#### Wan2.2 T2V Inference

For **Wan2.2 models** (`t2v-A14B`), you need to specify both low-noise and high-noise checkpoints:

```bash
python src/musubi_tuner/wan_generate_video.py --fp8 --task t2v-A14B --video_size 832 480 --video_length 81 --infer_steps 40 
--prompt "prompt for the video" --save_path path/to/save.mp4 --output_type both 
--dit path/to/wan2.2_t2v_A14B_low_noise.safetensors --dit_high_noise path/to/wan2.2_t2v_A14B_high_noise.safetensors
--vae path/to/wan_2.1_vae.safetensors --t5 path/to/models_t5_umt5-xxl-enc-bf16.pth 
--attn_mode torch
```

**Note**: Wan2.2 models use different default inference settings (40 steps, different flow shift values) optimized for the dual-checkpoint architecture.

`--task` is one of:
- **Wan2.1 models**: `t2v-1.3B`, `t2v-14B`, `i2v-14B`, `t2i-14B` (official models)
- **Wan2.1 Fun Control models**: `t2v-1.3B-FC`, `t2v-14B-FC`, `i2v-14B-FC`
- **Wan2.2 models**: `t2v-A14B`, `i2v-A14B` (enhanced 14B models with dual-checkpoint architecture)

`--attn_mode` is `torch`, `sdpa` (same as `torch`), `xformers`, `sageattn`,`flash2`, `flash` (same as `flash2`) or `flash3`. `torch` is the default. Other options require the corresponding library to be installed. `flash3` (Flash attention 3) is not tested.

Specifying `--fp8` runs DiT in fp8 mode. fp8 can significantly reduce memory consumption but may impact output quality.

`--fp8_scaled` can be specified in addition to `--fp8` to run the model in fp8 weights optimization. This increases memory consumption and speed slightly but improves output quality. See [here](advanced_config.md#fp8-weight-optimization-for-models--モデルの重みのfp8への最適化) for details.

`--fp8_fast` option is also available for faster inference on RTX 40x0 GPUs. This option requires `--fp8_scaled` option. **This option seems to degrade the output quality.**

`--fp8_t5` can be used to specify the T5 model in fp8 format. This option reduces memory usage for the T5 model.  

`--negative_prompt` can be used to specify a negative prompt. If omitted, the default negative prompt is used.

`--flow_shift` can be used to specify the flow shift (default 3.0 for I2V with 480p, 5.0 for others).

`--guidance_scale` can be used to specify the guidance scale for classifier free guidance (default 5.0).

`--blocks_to_swap` is the number of blocks to swap during inference. The default value is None (no block swap). The maximum value is 39 for 14B model and 29 for 1.3B model.

`--vae_cache_cpu` enables VAE cache in main memory. This reduces VRAM usage slightly but processing is slower.

`--compile` enables torch.compile. See [here](/README.md#inference) for details.

`--trim_tail_frames` can be used to trim the tail frames when saving. The default is 0.

`--cfg_skip_mode` specifies the mode for skipping CFG in different steps. The default is `none` (all steps).`--cfg_apply_ratio` specifies the ratio of steps where CFG is applied. See below for details.

`--include_patterns` and `--exclude_patterns` can be used to specify which LoRA modules to apply or exclude during training. If not specified, all modules are applied by default. These options accept regular expressions. 

`--include_patterns` specifies the modules to be applied, and `--exclude_patterns` specifies the modules to be excluded. The regular expression is matched against the LoRA key name, and include takes precedence.

The key name to be searched is in sd-scripts format (`lora_unet_<module_name with dot replaced by _>`). For example, `lora_unet_blocks_9_cross_attn_k`.

For example, if you specify `--exclude_patterns "blocks_[23]\d_"`, it will exclude modules containing `blocks_20` to `blocks_39`. If you specify `--include_patterns "cross_attn" --exclude_patterns "blocks_(0|1|2|3|4)_"`, it will apply LoRA to modules containing `cross_attn` and not containing `blocks_0` to `blocks_4`.

If you specify multiple LoRA weights, please specify them with multiple arguments. For example: `--include_patterns "cross_attn" ".*" --exclude_patterns "dummy_do_not_exclude" "blocks_(0|1|2|3|4)"`. `".*"` is a regex that matches everything. `dummy_do_not_exclude` is a dummy regex that does not match anything.

`--cpu_noise` generates initial noise on the CPU. This may result in the same results as ComfyUI with the same seed (depending on other settings).

If you are using the Fun Control model, specify the control video with `--control_path`. You can specify a video file or a folder containing multiple image files. The number of frames in the video file (or the number of images) should be at least the number specified in `--video_length` (plus 1 frame if you specify `--end_image_path`).

Please try to match the aspect ratio of the control video with the aspect ratio specified in `--video_size` (there may be some deviation from the initial image of I2V due to the use of bucketing processing).

Other options are same as `hv_generate_video.py` (some options are not supported, please check the help).

<details>
<summary>日本語</summary>
`--task` には以下のいずれかを指定します：
- **Wan2.1モデル**: `t2v-1.3B`, `t2v-14B`, `i2v-14B`, `t2i-14B` （公式モデル）
- **Wan2.1 Fun Controlモデル**: `t2v-1.3B-FC`, `t2v-14B-FC`, `i2v-14B-FC`
- **Wan2.2モデル**: `t2v-A14B`, `i2v-A14B` （デュアルチェックポイントアーキテクチャを持つ拡張14Bモデル）

`--attn_mode` には `torch`, `sdpa`（`torch`と同じ）、`xformers`, `sageattn`, `flash2`, `flash`（`flash2`と同じ）, `flash3` のいずれかを指定します。デフォルトは `torch` です。その他のオプションを使用する場合は、対応するライブラリをインストールする必要があります。`flash3`（Flash attention 3）は未テストです。

`--fp8` を指定するとDiTモデルをfp8形式で実行します。fp8はメモリ消費を大幅に削減できますが、出力品質に影響を与える可能性があります。
    
`--fp8_scaled` を `--fp8` と併用すると、fp8への重み量子化を行います。メモリ消費と速度はわずかに悪化しますが、出力品質が向上します。詳しくは[こちら](advanced_config.md#fp8-weight-optimization-for-models--モデルの重みのfp8への最適化)を参照してください。

`--fp8_fast` オプションはRTX 40x0 GPUでの高速推論に使用されるオプションです。このオプションは `--fp8_scaled` オプションが必要です。**出力品質が劣化するようです。**

`--fp8_t5` を指定するとT5モデルをfp8形式で実行します。T5モデル呼び出し時のメモリ使用量を削減します。

`--negative_prompt` でネガティブプロンプトを指定できます。省略した場合はデフォルトのネガティブプロンプトが使用されます。

`--flow_shift` でflow shiftを指定できます（480pのI2Vの場合はデフォルト3.0、それ以外は5.0）。

`--guidance_scale` でclassifier free guianceのガイダンススケールを指定できます（デフォルト5.0）。

`--blocks_to_swap` は推論時のblock swapの数です。デフォルト値はNone（block swapなし）です。最大値は14Bモデルの場合39、1.3Bモデルの場合29です。

`--vae_cache_cpu` を有効にすると、VAEのキャッシュをメインメモリに保持します。VRAM使用量が多少減りますが、処理は遅くなります。

`--compile`でtorch.compileを有効にします。詳細については[こちら](/README.md#inference)を参照してください。

`--trim_tail_frames` で保存時に末尾のフレームをトリミングできます。デフォルトは0です。

`--cfg_skip_mode` は異なるステップでCFGをスキップするモードを指定します。デフォルトは `none`（全ステップ）。`--cfg_apply_ratio` はCFGが適用されるステップの割合を指定します。詳細は後述します。

LoRAのどのモジュールを適用するかを、`--include_patterns`と`--exclude_patterns`で指定できます（未指定時・デフォルトは全モジュール適用されます
）。これらのオプションには、正規表現を指定します。`--include_patterns`は適用するモジュール、`--exclude_patterns`は適用しないモジュールを指定します。正規表現がLoRAのキー名に含まれるかどうかで判断され、includeが優先されます。

検索対象となるキー名は sd-scripts 形式（`lora_unet_<モジュール名のドットを_に置換したもの>`）です。例：`lora_unet_blocks_9_cross_attn_k`

たとえば `--exclude_patterns "blocks_[23]\d_"`のみを指定すると、`blocks_20`から`blocks_39`を含むモジュールが除外されます。`--include_patterns "cross_attn" --exclude_patterns "blocks_(0|1|2|3|4)_"`のようにincludeとexcludeを指定すると、`cross_attn`を含むモジュールで、かつ`blocks_0`から`blocks_4`を含まないモジュールにLoRAが適用されます。

複数のLoRAの重みを指定する場合は、複数個の引数で指定してください。例：`--include_patterns "cross_attn" ".*" --exclude_patterns "dummy_do_not_exclude" "blocks_(0|1|2|3|4)"` `".*"`は全てにマッチする正規表現です。`dummy_do_not_exclude`は何にもマッチしないダミーの正規表現です。

`--cpu_noise`を指定すると初期ノイズをCPUで生成します。これにより同一seed時の結果がComfyUIと同じになる可能性があります（他の設定にもよります）。

Fun Controlモデルを使用する場合は、`--control_path`で制御用の映像を指定します。動画ファイル、または複数枚の画像ファイルを含んだフォルダを指定できます。動画ファイルのフレーム数（または画像の枚数）は、`--video_length`で指定したフレーム数以上にしてください（後述の`--end_image_path`を指定した場合は、さらに+1フレーム）。

制御用の映像のアスペクト比は、`--video_size`で指定したアスペクト比とできるかぎり合わせてください（bucketingの処理を流用しているためI2Vの初期画像とズレる場合があります）。

その他のオプションは `hv_generate_video.py` と同じです（一部のオプションはサポートされていないため、ヘルプを確認してください）。
</details>

#### CFG Skip Mode / CFGスキップモード

 These options allow you to balance generation speed against prompt accuracy. More skipped steps results in faster generation with potential quality degradation.

Setting `--cfg_apply_ratio` to 0.5 speeds up the denoising loop by up to 25%.

`--cfg_skip_mode` specified one of the following modes:

- `early`: Skips CFG in early steps for faster generation, applying guidance mainly in later refinement steps
- `late`: Skips CFG in later steps, applying guidance during initial structure formation
- `middle`: Skips CFG in middle steps, applying guidance in both early and later steps
- `early_late`: Skips CFG in both early and late steps, applying only in middle steps
- `alternate`: Applies CFG in alternate steps based on the specified ratio
- `none`: Applies CFG at all steps (default)

`--cfg_apply_ratio` specifies a value from 0.0 to 1.0 controlling the proportion of steps where CFG is applied. For example, setting 0.5 means CFG will be applied in only 50% of the steps.

If num_steps is 10, the following table shows the steps where CFG is applied based on the `--cfg_skip_mode` option (A means CFG is applied, S means it is skipped, `--cfg_apply_ratio` is 0.6):

| skip mode | CFG apply pattern |
|---|---|
| early | SSSSAAAAAA |
| late | AAAAAASSSS |
| middle | AAASSSSAAA |
| early_late | SSAAAAAASS |
| alternate | SASASAASAS |

The appropriate settings are unknown, but you may want to try `late` or `early_late` mode with a ratio of around 0.3 to 0.5.
<details>
<summary>日本語</summary>
これらのオプションは、生成速度とプロンプトの精度のバランスを取ることができます。スキップされるステップが多いほど、生成速度が速くなりますが、品質が低下する可能性があります。

ratioに0.5を指定することで、デノイジングのループが最大25%程度、高速化されます。

`--cfg_skip_mode` は次のモードのいずれかを指定します：

- `early`：初期のステップでCFGをスキップして、主に終盤の精細化のステップで適用します
- `late`：終盤のステップでCFGをスキップし、初期の構造が決まる段階で適用します
- `middle`：中間のステップでCFGをスキップし、初期と終盤のステップの両方で適用します
- `early_late`：初期と終盤のステップの両方でCFGをスキップし、中間のステップのみ適用します
- `alternate`：指定された割合に基づいてCFGを適用します

`--cfg_apply_ratio` は、CFGが適用されるステップの割合を0.0から1.0の値で指定します。たとえば、0.5に設定すると、CFGはステップの50%のみで適用されます。

具体的なパターンは上のテーブルを参照してください。

適切な設定は不明ですが、モードは`late`または`early_late`、ratioは0.3~0.5程度から試してみると良いかもしれません。
</details>

#### Skip Layer Guidance

Skip Layer Guidance is a feature that uses the output of a model with some blocks skipped as the unconditional output of classifier free guidance. It was originally proposed in [SD 3.5](https://github.com/comfyanonymous/ComfyUI/pull/5404) and first applied in Wan2GP in [this PR](https://github.com/deepbeepmeep/Wan2GP/pull/61). It may improve the quality of generated videos.

The implementation of SD 3.5 is [here](https://github.com/Stability-AI/sd3.5/blob/main/sd3_impls.py), and the implementation of Wan2GP (the PR mentioned above) has some different specifications. This inference script allows you to choose between the two methods.

*The SD3.5 method applies slg output in addition to cond and uncond (slows down the speed). The Wan2GP method uses only cond and slg output.*

The following arguments are available:

- `--slg_mode`: Specifies the SLG mode. `original` for SD 3.5 method, `uncond` for Wan2GP method. Default is None (no SLG).
- `--slg_layers`: Specifies the indices of the blocks (layers) to skip in SLG, separated by commas. Example: `--slg_layers 4,5,6`. Default is empty (no skip). If this option is not specified, `--slg_mode` is ignored.
- `--slg_scale`: Specifies the scale of SLG when `original`. Default is 3.0.
- `--slg_start`: Specifies the start step of SLG application in inference steps from 0.0 to 1.0. Default is 0.0 (applied from the beginning).
- `--slg_end`: Specifies the end step of SLG application in inference steps from 0.0 to 1.0. Default is 0.3 (applied up to 30% from the beginning).

Appropriate settings are unknown, but you may want to try `original` mode with a scale of around 3.0 and a start ratio of 0.0 and an end ratio of 0.5, with layers 4, 5, and 6 skipped.

<details>
<summary>日本語</summary>
Skip Layer Guidanceは、一部のblockをスキップしたモデル出力をclassifier free guidanceのunconditional出力に使用する機能です。元々は[SD 3.5](https://github.com/comfyanonymous/ComfyUI/pull/5404)で提案されたもので、Wan2.1には[Wan2GPのこちらのPR](https://github.com/deepbeepmeep/Wan2GP/pull/61)で初めて適用されました。生成動画の品質が向上する可能性があります。

SD 3.5の実装は[こちら](https://github.com/Stability-AI/sd3.5/blob/main/sd3_impls.py)で、Wan2GPの実装（前述のPR）は一部仕様が異なります。この推論スクリプトでは両者の方式を選択できるようになっています。

※SD3.5方式はcondとuncondに加えてslg outputを適用します（速度が低下します）。Wan2GP方式はcondとslg outputのみを使用します。

以下の引数があります。

- `--slg_mode`：SLGのモードを指定します。`original`でSD 3.5の方式、`uncond`でWan2GPの方式です。デフォルトはNoneで、SLGを使用しません。
- `--slg_layers`：SLGでスキップするblock (layer)のインデクスをカンマ区切りで指定します。例：`--slg_layers 4,5,6`。デフォルトは空（スキップしない）です。このオプションを指定しないと`--slg_mode`は無視されます。
- `--slg_scale`：`original`のときのSLGのスケールを指定します。デフォルトは3.0です。
- `--slg_start`：推論ステップのSLG適用開始ステップを0.0から1.0の割合で指定します。デフォルトは0.0です（最初から適用）。
- `--slg_end`：推論ステップのSLG適用終了ステップを0.0から1.0の割合で指定します。デフォルトは0.3です（最初から30%まで適用）。

適切な設定は不明ですが、`original`モードでスケールを3.0程度、開始割合を0.0、終了割合を0.5程度に設定し、4, 5, 6のlayerをスキップする設定から始めると良いかもしれません。
</details>

### I2V Inference / I2V推論

#### Wan2.1 I2V Inference

The following is an example of Wan2.1 I2V inference (input as a single line):

```bash
python src/musubi_tuner/wan_generate_video.py --fp8 --task i2v-14B --video_size 832 480 --video_length 81 --infer_steps 20 
--prompt "prompt for the video" --save_path path/to/save.mp4 --output_type both 
--dit path/to/wan2.1_i2v_480p_14B_bf16_etc.safetensors --vae path/to/wan_2.1_vae.safetensors 
--t5 path/to/models_t5_umt5-xxl-enc-bf16.pth --clip path/to/models_clip_open-clip-xlm-roberta-large-vit-huge-14.pth 
--attn_mode torch --image_path path/to/image.jpg
```

#### Wan2.2 I2V Inference

For **Wan2.2 I2V models** (`i2v-A14B`), you need to specify both checkpoints:

```bash
python src/musubi_tuner/wan_generate_video.py --fp8 --task i2v-A14B --video_size 832 480 --video_length 81 --infer_steps 40 
--prompt "prompt for the video" --save_path path/to/save.mp4 --output_type both 
--dit path/to/wan2.2_i2v_A14B_low_noise.safetensors --dit_high_noise path/to/wan2.2_i2v_A14B_high_noise.safetensors
--vae path/to/wan_2.1_vae.safetensors --t5 path/to/models_t5_umt5-xxl-enc-bf16.pth 
--clip path/to/models_clip_open-clip-xlm-roberta-large-vit-huge-14.pth --attn_mode torch --image_path path/to/image.jpg
```

Add `--clip` to specify the CLIP model. `--image_path` is the path to the image to be used as the initial frame.

`--end_image_path` can be used to specify the end image. This option is experimental. When this option is specified, the saved video will be slightly longer than the specified number of frames and will have noise, so it is recommended to specify `--trim_tail_frames 3` to trim the tail frames.

You can also use the Fun Control model for I2V inference. Specify the control video with `--control_path`. 

Other options are same as T2V inference.

<details>
<summary>日本語</summary>
`--clip` を追加してCLIPモデルを指定します。`--image_path` は初期フレームとして使用する画像のパスです。

`--end_image_path` で終了画像を指定できます。このオプションは実験的なものです。このオプションを指定すると、保存される動画が指定フレーム数よりもやや多くなり、かつノイズが乗るため、`--trim_tail_frames 3` などを指定して末尾のフレームをトリミングすることをお勧めします。

I2V推論でもFun Controlモデルが使用できます。`--control_path` で制御用の映像を指定します。

その他のオプションはT2V推論と同じです。
</details>

### New Batch and Interactive Modes / 新しいバッチモードとインタラクティブモード

In addition to single video generation, Wan 2.1 now supports batch generation from file and interactive prompt input:

#### Batch Mode from File / ファイルからのバッチモード

Generate multiple videos from prompts stored in a text file:

```bash
python src/musubi_tuner/wan_generate_video.py --from_file prompts.txt --task t2v-14B 
--dit path/to/model.safetensors --vae path/to/vae.safetensors 
--t5 path/to/t5_model.pth --save_path output_directory
```

The prompts file format:
- One prompt per line
- Empty lines and lines starting with # are ignored (comments)
- Each line can include prompt-specific parameters using command-line style format:

```
A beautiful sunset over mountains --w 832 --h 480 --f 81 --d 42 --s 20
A busy city street at night --w 480 --h 832 --g 7.5 --n low quality, blurry
```

Supported inline parameters (if ommitted, default values from the command line are used):
- `--w`: Width
- `--h`: Height
- `--f`: Frame count
- `--d`: Seed
- `--s`: Inference steps
- `--g` or `--l`: Guidance scale
- `--fs`: Flow shift
- `--i`: Image path (for I2V)
- `--cn`: Control path (for Fun Control)
- `--n`: Negative prompt

In batch mode, models are loaded once and reused for all prompts, significantly improving overall generation time compared to multiple single runs.

#### Interactive Mode / インタラクティブモード

Interactive command-line interface for entering prompts:

```bash
python src/musubi_tuner/wan_generate_video.py --interactive --task t2v-14B 
--dit path/to/model.safetensors --vae path/to/vae.safetensors 
--t5 path/to/t5_model.pth --save_path output_directory
```

In interactive mode:
- Enter prompts directly at the command line
- Use the same inline parameter format as batch mode
- Use Ctrl+D (or Ctrl+Z on Windows) to exit
- Models remain loaded between generations for efficiency

<details>
<summary>日本語</summary>
単一動画の生成に加えて、Wan 2.1は現在、ファイルからのバッチ生成とインタラクティブなプロンプト入力をサポートしています。

#### ファイルからのバッチモード

テキストファイルに保存されたプロンプトから複数の動画を生成します：

```bash
python src/musubi_tuner/wan_generate_video.py --from_file prompts.txt --task t2v-14B 
--dit path/to/model.safetensors --vae path/to/vae.safetensors 
--t5 path/to/t5_model.pth --save_path output_directory
```

プロンプトファイルの形式：
- 1行に1つのプロンプト
- 空行や#で始まる行は無視されます（コメント）
- 各行にはコマンドライン形式でプロンプト固有のパラメータを含めることができます：

サポートされているインラインパラメータ（省略した場合、コマンドラインのデフォルト値が使用されます）
- `--w`: 幅
- `--h`: 高さ
- `--f`: フレーム数
- `--d`: シード
- `--s`: 推論ステップ
- `--g` または `--l`: ガイダンススケール
- `--fs`: フローシフト
- `--i`: 画像パス（I2V用）
- `--cn`: コントロールパス（Fun Control用）
- `--n`: ネガティブプロンプト

バッチモードでは、モデルは一度だけロードされ、すべてのプロンプトで再利用されるため、複数回の単一実行と比較して全体的な生成時間が大幅に改善されます。

#### インタラクティブモード

プロンプトを入力するためのインタラクティブなコマンドラインインターフェース：

```bash
python src/musubi_tuner/wan_generate_video.py --interactive --task t2v-14B 
--dit path/to/model.safetensors --vae path/to/vae.safetensors 
--t5 path/to/t5_model.pth --save_path output_directory
```

インタラクティブモードでは：
- コマンドラインで直接プロンプトを入力
- バッチモードと同じインラインパラメータ形式を使用
- 終了するには Ctrl+D (Windowsでは Ctrl+Z) を使用
- 効率のため、モデルは生成間で読み込まれたままになります
</details>

