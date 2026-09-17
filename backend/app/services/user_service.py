from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    def get(self, db: Session, user_id: int) -> Optional[User]:
        """Fetch a single user by primary key ID."""
        return db.get(User, user_id)

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        """Fetch a user by email address."""
        stmt = select(User).where(User.email == email)
        return db.scalar(stmt)

    def get_multi(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[User]:
        """Fetch a paginated list of users."""
        stmt = select(User).offset(skip).limit(limit)
        return list(db.scalars(stmt).all())

    def create(self, db: Session, obj_in: UserCreate) -> User:
        """Create a new user with securely hashed password."""
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_active=True,
            is_superuser=False,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, db_obj: User, obj_in: UserUpdate
    ) -> User:
        """Update existing user properties."""
        update_data = obj_in.model_dump(exclude_unset=True)
        if "password" in update_data and update_data["password"]:
            hashed_password = get_password_hash(update_data.pop("password"))
            db_obj.hashed_password = hashed_password

        for field, value in update_data.items():
            setattr(db_obj, field, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(
        self, db: Session, email: str, password: str
    ) -> Optional[User]:
        """Authenticate user by email and password."""
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


user_service = UserService()
