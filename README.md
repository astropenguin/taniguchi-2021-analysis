# taniguchi-2021-analysis
Analysis repository for Taniguchi et al. 2021, AJ, 162, 111

## How to use

1. Install [VS Code] and [Docker Desktop], and launch them
1. Install the [Remote Containers] extension to VS Code
1. Clone this repository
1. Put datasets (*.nc) in `./data`
1. Open the repository by VS Code
1. Choose `Reopen in Container` from the [Command Palette]

## Notes

| Note no. | Data | Products | Has plots? | Description |
| --- | --- | --- | --- | --- |
| [2020-02-26](notes/2020-02-26) | PJ020941.3 | n/a | yes | GoDec（のバリエーション）を使ってON-Rの操作からノイズ除去と強度較正を試した。Sparseを求める際、メジアンフィルターを使って周波数方向にTVに対応する操作を行ったら上手くいった。本物のTVを入れても良いかもしれない。 |
| [2020-04-27](notes/2020-04-27) | n/a | n/a | yes | 論文用のL+S decompositionとGoDec algorithmの概念図を作成した。 |
| [2020-05-07](notes/2020-05-07) | PJ020941.3 | n/a | yes | 論文用のPJ020941.3の作図を行った。関数の引数等を論文に合わせた。 |
| [2021-05-24](notes/2021-05-24) | PJ020941.3 | n/a | yes | PJ020941.3観測のOFF点情報やON-OFF移動時間などをログから求めた。 |

[Command Palette]: https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette
[Docker Desktop]: https://www.docker.com/products/docker-desktop
[Remote Containers]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
[VS Code]: https://code.visualstudio.com
