// pages/history/history.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
  
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;

    // var  historylist = [
    //   {
    //     id:0,
    //     date: '2015年5月1日',
    //     title: '武汉分校成立',
    //     imgurl: "http://localhost/images/D4.png",
    //     desc:"北京市海淀外国语实验学校的办学思路从成立之初就十分明确，“外国语”体现了“面向世界，走国际化办学道路”的宗旨；而“实验”则是一种开放的姿态，表达了学校力争成为中国民办基础教育领域开拓者的决心。"
    //   },
    //   {
    //     id: 1,
    //     date: '2016年6月1日',
    //     title: '武汉分校',
    //     imgurl: "http://localhost/images/D5.png",
    //   }
    // ];
    wx.request({
      url: 'http://localhost:8000/gethistory/',
      method:'GET',
      header:{
        'content-type': 'application/json'
      },
      success:function(res){
        console.log(res.data);
        that.setData({
          historylist: res.data,
        })
      }
    })
    // this.setData({
    //   historylist:historylist,
    // });
  
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})