<template>
  <div class="Intro">
    <div class="Intro-MainImgWrap">
      <img class="Intro-MainImgWrap-Img" src="../assets/profile.jpg" />
    </div>
    <div class="Intro-Title">손민재</div>
    <div class="Intro-SubTitle">Front-End-Dev In DGSW, Team B1ND</div>
    <div class="Intro-Content">
      대구 소프트웨어 고등학교 2학년 2반 9번 손민재입니다. 웹 Front-End 분야를
      공부하고 있으며 교내 동아리 B1ND의 웹팀 팀장을 맡고 있습니다. 편리함을
      추구하는 개발자가 되기위해 노력하고 있습니다.
    </div>
    <div class="Intro-IconWrap">
      <a class="Intro-Icons" href="https://github.com/Clzzi" target="_blank"
        ><img class="Intro-Icon" src="../assets/github.svg"
      /></a>
      <a class="Intro-Icons" href="https://velog.io/@jce1407" target="_blank"
        ><img class="Intro-Icon" src="../assets/velog.jpg"
      /></a>
    </div>
    <hr />
    <div class="Intro-StackTitle">STACK</div>
    <div class="Intro-StackWrap">
      <img class="Intro-Stack" src="../assets/react.svg" />
      <img class="Intro-Stack" src="../assets/sass.svg" />
      <img class="Intro-Stack" src="../assets/typescript.svg" />
      <img class="Intro-Stack" src="../assets/htmlcss.svg" />
      <img class="Intro-Stack" src="../assets/javascript.svg" />
    </div>
  </div>
</template>

<script>
</script>

<style scoped lang="scss">
.Intro {
  margin-top: 80px;
  display: inline-block;
  width: 840px;
  height: 540px;
  justify-content: center;
  text-align: center;
  align-items: center;
  vertical-align: middle;
  &-MainImgWrap {
    display: inline-block;
    margin-bottom: 10px;

    &-Img {
      width: 25%;
      border-radius: 50%;
      box-shadow: 1px 1px 5px black;
    }
  }
  &-Title {
    font-size: 2rem;
    font-weight: 600;
  }
  &-SubTitle {
    font-size: 1.5rem;
    color: gray;
    margin-bottom: 15px;
  }
  &-Content {
    font-size: 1rem;
    color: black;
    line-height: 20px;
    word-spacing: 1.5px;
    margin-bottom: 15px;
  }

  &-StackTitle {
    font-size: 2rem;
    font-weight: bold;
    margin-top: 15px;
  }

  &-StacksWrap {
    display: flex;
    justify-content: center;
    text-align: center;
    align-items: center;
    vertical-align: middle;
  }

  &-Stack {
    width: 100px;
    height: 100px;
    margin-right: 10px;
  }
  &-Icon {
    width: 100px;
    height: 100px;
    margin-right: 15px;
  }
}
</style>