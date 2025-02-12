from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from orm.database import Base
from orm.mixins import RecordTimestamps
from .user_post_reaction import UserPostReaction, ReactionType
from .comment import Comment
from sqlalchemy.orm import Session


class Post(Base, RecordTimestamps):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    univers_id = Column(Integer, ForeignKey("univers.id"), nullable=False)

    title = Column(String, nullable=False)  # Title of the post
    description = Column(String, nullable=True)  # Description of the post
    user_rating = Column(Integer, nullable=True)  # User's rating (e.g., 1-5)
    other_ratings_count = Column(
        Integer, default=0
    )  # Count of ratings from other users
    likes = Column(Integer, default=0)  # Number of likes
    dislikes = Column(Integer, default=0)  # Number of dislikes

    user = relationship("User", back_populates="posts")
    univers = relationship("Univers", back_populates="posts")
    photos = relationship("Photo", back_populates="post", cascade="all, delete-orphan")
    reactions = relationship("UserPostReaction", back_populates="post")
    comments = relationship(
        "Comment", back_populates="post", cascade="all, delete-orphan"
    )

    def add_reaction(self, db: Session, user_id: int, reaction_type: ReactionType):
        """Ajoute un like ou un dislike pour un utilisateur donné."""
        existing_reaction = (
            db.query(UserPostReaction)
            .filter_by(user_id=user_id, post_id=self.id)
            .first()
        )

        if existing_reaction:
            if existing_reaction.reaction == reaction_type:
                return
            else:
                db.delete(existing_reaction)
                if reaction_type == ReactionType.LIKE:
                    self.likes += 1
                    self.dislikes -= 1
                elif reaction_type == ReactionType.DISLIKE:
                    self.dislikes += 1
                    self.likes -= 1
        else:
            new_reaction = UserPostReaction(
                user_id=user_id, post_id=self.id, reaction=reaction_type
            )
            db.add(new_reaction)
            if reaction_type == ReactionType.LIKE:
                self.likes += 1
            elif reaction_type == ReactionType.DISLIKE:
                self.dislikes += 1
