package com.sachin.designpattern.demo.strategy;

public abstract class CameraApp {
    ShareStrategy shareStrategy;

    public abstract void edit();

    public void take() {
        System.out.println("taking photo");
    }

    public void save() {
        System.out.println("saving photo");
    }

    public void share() {
        shareStrategy.share();
    }

    public void setShareStrategy(ShareStrategy shareStrategy) {
        this.shareStrategy = shareStrategy;
    }
}
