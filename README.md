# Rigging: Rigging tools for Maya

### What is it?
#### CreatFKController
- reateFKControllerツールはSelectされているJointに自動的にCircleのControllerを付けてくれる基礎的なToolです。
- Pythonを学び始め一番最初に作ったToolです。
#### AutoControllerChaser
- AutoControllerChaserツールは自分がカスタマイズしたControllerを選択したJointに自動的に付けてくれるToolです。特徴としては、Joint自体にTranslate、Radius、Scaleに数値が入ってもアニメーションを付けるには問題ないようにしました。
- ダウンロードしたモデリングのJointに異常があったので、これらを問題ない環境でアニメーションを付けるようにこのようなToolを作りました。
#### TrianglePolygonFinder
- TrianglePolygonFinderツールはModelingの中にTriangleのPolygonを探して表示してくれるToolです。
- ダウンロードしたモデリングにあまりにもTriangle polygonが多かったためこれらを探し、直すためこのようなツールを作りました。
### How to work?
#### CreatFKController
1. CircleControllerを付けたいJoint達をSelectします。
2. Scriptを実行させます。
3. orientconstraintまで適用されているControllerがJointにConstraintされました。
#### AutoControllerChaser
1. 自分が使いたいFKControllerを一つ作ります。
2. 作ったControllerとJointをSeletします。
3. Scriptを実行させます。
(カスタマイズしたControllerは必ず(0,0,0)にいなければうまく起動しません)
#### TrianglePolygonFinder
1. TrianglePolygonを探したいModelingをSelectします。
2. Scriptを実行させます。
3. Serch Triangleをクリックします。
4. Triangle Polygonと共有するEdgeを持っているPolygonを同時に見せてくれます。自動的にIsolateされますので直した後、Isolate seletを解除します。これでTirangle polygonをもっと簡単に直すことができます。
### Demo
#### CreatFKContoller
![Joint1]https://raw.githubusercontent.com/eeeeuci/Rigging/main/img/Joint1.png
#### AutoControllerChaser

#### TrianglePolygonFinder

### License
MIT