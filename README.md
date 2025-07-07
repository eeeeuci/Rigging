# Rigging: Rigging tools for Maya

### What is it?
#### CreatFKController
- reateFKControllerツールはSelectされているJointに自動的にCircleのControllerを付けてくれる基礎的なToolです。
- Pythonを学び始め一番最初に作ったToolです。
#### AutoControllerChaser
- AutoControllerChaserツールはControllerを選択してJointに自動的に付けてくれるToolです。特徴としては、Joint自体にTranslate、Radius、Scaleに数値が入ってもアニメーションを付けるには問題ないようにしました。
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
1. Controllerを付けたいJointをSelectします。
2. Toolを実行させて付けたいControllerの形を選びます。
3. 実行させたら、選択したJointにControllerが付いているのを確認します。
4. F8でControllerを選択し形を変えてカスタマイズします。 
(カスタマイズしたControllerは必ず(0,0,0)にいなければうまく起動しません)
#### TrianglePolygonFinder
1. TrianglePolygonを探したいModelingをSelectします。
2. Scriptを実行させます。
3. Serch Triangleをクリックします。
4. Triangle Polygonと共有するEdgeを持っているPolygonを同時に見せてくれます。自動的にIsolateされますので直した後、Isolate seletを解除します。これでTirangle polygonをもっと簡単に直すことができます。
### Demo
#### CreatFKContoller
![Joint1](https://github.com/user-attachments/assets/02234775-4ccd-4b48-a307-f5ede2e37c86)
![Joint2](https://github.com/user-attachments/assets/563838b0-3377-4a76-9db6-6d00a4320c96)
#### AutoControllerChaser

#### TrianglePolygonFinder

### License
MIT