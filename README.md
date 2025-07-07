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
![Atrribute](https://github.com/user-attachments/assets/92b2e12f-5685-479f-91b8-23a31a2f7887)
![UI](https://github.com/user-attachments/assets/8c3d4659-7565-4c24-89fc-d4a58f4d611f)
![Chaser](https://github.com/user-attachments/assets/9b79b931-1d50-463e-a6c0-56281c23f4bc)
- 左はCircle、右はSquarでControllerを付けた場合。
#### TrianglePolygonFinder
![Trianglemodeling](https://github.com/user-attachments/assets/a6f48ca9-86c9-4db3-8ee7-b0ce1529ebe4)
![UI2](https://github.com/user-attachments/assets/fc704e35-b215-4d53-bdab-c385fb83e223)
![Trianglemodeling2](https://github.com/user-attachments/assets/127e9897-90ce-45fe-be86-9da897c880bb)
![UI3](https://github.com/user-attachments/assets/856b2e57-decb-4ee6-88c6-0d62ed55dea5)
![trianglemodeling3](https://github.com/user-attachments/assets/2dad0f7f-f64b-4231-b3d5-b4e4d02146b0)
### License
MIT